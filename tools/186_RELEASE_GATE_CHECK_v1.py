#!/usr/bin/env python3
"""Fail-closed evidence gate for a specific offline questionnaire HTML release candidate.

This checks evidence metadata/integrity, not the underlying clinical or browser tests.
No third-party packages. Never uploads or publishes anything.
"""
import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

REQUIRED = {
    'structural': [
        'question_bank_sections', 'unique_ids_codes', 'conditional_dependencies',
        'scoring_and_safety_semantics', 'offline_self_contained', 'backup_schema_compatibility',
    ],
    'behavior': [
        'start_and_section_navigation', 'selection_does_not_autosave', 'save_next_and_resume',
        'conditional_branches_and_skips', 'backup_download_and_restore',
        'language_switch_keeps_answers', 'doctor_and_ai_exports', 'a4_summary_and_print',
        'safety_prompts_and_help', 'offline_android_chrome', 'old_backup_migration',
    ],
    'translation': [
        'all_questions_and_choices', 'all_interface_buttons_navigation',
        'all_reports_exports_and_filenames', 'instructions_legal_resources_privacy',
        'no_missing_or_unmarked_fallbacks', 'sensitive_wording_review_recorded',
    ],
    'safety': [
        'no_diagnosis_or_automatic_suicide_risk_score',
        'correct_emergency_and_medical_disclaimers',
    ],
}
REVIEW_LABEL = 'review_candidate_label_visible'
HEX64 = re.compile(r'^[a-f0-9]{64}$')
ISO_UTC = re.compile(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$')


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def verify(candidate, evidence_file, mode):
    errors = []
    if not candidate.is_file() or candidate.suffix.lower() != '.html':
        return ['Missing/invalid candidate HTML file']
    if not evidence_file.is_file():
        return ['Missing evidence JSON']
    try:
        doc = json.loads(evidence_file.read_text(encoding='utf-8'))
    except (ValueError, UnicodeError, OSError) as e:
        return [f'Unreadable evidence JSON: {e}']
    if not isinstance(doc, dict):
        return ['Evidence must be a JSON object']
    if doc.get('schema') != 'questionnaire-release-gate-1':
        errors.append('Unsupported/missing evidence schema')
    if doc.get('mode') != mode:
        errors.append('Mode mismatch between evidence and command')
    expected = sha(candidate)
    if doc.get('candidate_sha256') != expected:
        errors.append(f'Candidate checksum mismatch; current SHA256 is {expected}')
    if doc.get('candidate_name') != candidate.name:
        errors.append('Candidate filename mismatch')
    tests = doc.get('tests')
    if not isinstance(tests, dict):
        return errors + ['Missing tests object']
    required = {k for values in REQUIRED.values() for k in values}
    if mode == 'professional_review':
        required.add(REVIEW_LABEL)
    for test_id in sorted(required):
        item = tests.get(test_id)
        if not isinstance(item, dict):
            errors.append(f'{test_id}: missing test record')
            continue
        if item.get('status') != 'PASS':
            errors.append(f'{test_id}: not PASS (status={item.get("status", "missing")})')
            continue
        for field in ('tester', 'method', 'checked_at', 'evidence_file', 'evidence_sha256'):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f'{test_id}: missing {field}')
        if not isinstance(item.get('checked_at'), str) or not ISO_UTC.fullmatch(item.get('checked_at')):
            errors.append(f'{test_id}: checked_at must be UTC YYYY-MM-DDTHH:MM:SSZ')
        report = item.get('evidence_file', '')
        if not isinstance(report, str):
            continue
        # Forbid paths outside the evidence folder; all evidence is packaged locally.
        report_path = (evidence_file.parent / report).resolve()
        if not report_path.is_relative_to(evidence_file.parent.resolve()):
            errors.append(f'{test_id}: evidence file escapes evidence directory')
        elif not report_path.is_file():
            errors.append(f'{test_id}: evidence file not found: {report}')
        elif sha(report_path) != item.get('evidence_sha256'):
            errors.append(f'{test_id}: evidence checksum mismatch')
    if mode == 'public_release':
        review = doc.get('clinical_review')
        if not isinstance(review, dict) or review.get('status') != 'COMPLETE':
            errors.append('Clinical human review is missing/incomplete for public release')
        else:
            for field in ('reviewer_name', 'credentials', 'scope', 'date', 'decision', 'evidence_file', 'evidence_sha256'):
                if not isinstance(review.get(field), str) or not review[field].strip():
                    errors.append(f'Clinical review missing {field}')
            if review.get('decision') != 'APPROVED_WITH_DOCUMENTED_LIMITATIONS':
                errors.append('Clinical review decision does not approve this candidate for public release')
            p = review.get('evidence_file', '')
            if isinstance(p, str):
                full = (evidence_file.parent / p).resolve()
                if not full.is_relative_to(evidence_file.parent.resolve()) or not full.is_file():
                    errors.append('Clinical review evidence file missing/unsafe')
                elif sha(full) != review.get('evidence_sha256'):
                    errors.append('Clinical review evidence checksum mismatch')
    return errors


def self_test():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        candidate = root / 'test.html'
        candidate.write_text('<html lang="lv"></html>', encoding='utf-8')
        report = root / 'actual-test-report.txt'
        report.write_text('Synthetic unit test fixture — NOT real questionnaire test evidence.', encoding='utf-8')
        base = {'schema': 'questionnaire-release-gate-1', 'mode': 'professional_review',
                'candidate_name': candidate.name, 'candidate_sha256': sha(candidate),
                'tests': {}}
        evidence = root / 'evidence.json'
        evidence.write_text(json.dumps(base))
        assert verify(candidate, evidence, 'professional_review'), 'Pending evidence must block release'
        template = dict(base)
        template['tests'] = {
            key: {'status': 'PASS', 'tester': 'synthetic-fixture', 'method': 'synthetic-fixture',
                  'checked_at': '2026-11-05T00:00:00Z', 'evidence_file': report.name,
                  'evidence_sha256': sha(report)}
            for values in REQUIRED.values() for key in values
        }
        template['tests'][REVIEW_LABEL] = template['tests']['question_bank_sections'].copy()
        evidence.write_text(json.dumps(template))
        assert not verify(candidate, evidence, 'professional_review'), 'Complete fixture should pass gate schema'
        candidate.write_text('<html lang="en"></html>')
        assert any('Candidate checksum mismatch' in e for e in verify(candidate, evidence, 'professional_review'))
        candidate.write_text('<html lang="lv"></html>')
        template['tests']['question_bank_sections']['status'] = 'PENDING'
        evidence.write_text(json.dumps(template))
        assert any('question_bank_sections: not PASS' in e for e in verify(candidate, evidence, 'professional_review'))
        template['tests']['question_bank_sections']['status'] = 'PASS'
        evidence.write_text(json.dumps(template))
        template['mode'] = 'public_release'
        evidence.write_text(json.dumps(template))
        assert any('Clinical human review is missing' in e for e in verify(candidate, evidence, 'public_release')), 'Public mode requires clinical review'
        template['clinical_review'] = {
            'status':'COMPLETE', 'reviewer_name':'synthetic-fixture', 'credentials':'synthetic-fixture',
            'scope':'synthetic-fixture', 'date':'2026-11-05',
            'decision':'APPROVED_WITH_DOCUMENTED_LIMITATIONS',
            'evidence_file':report.name, 'evidence_sha256':sha(report),
        }
        evidence.write_text(json.dumps(template))
        assert not verify(candidate, evidence, 'public_release'), 'Complete public fixture should pass schema gate'
    print('PASS: gate self-test (missing evidence, candidate change, pending test, and missing clinical review block release)')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate', type=Path)
    p.add_argument('--evidence', type=Path)
    p.add_argument('--mode', choices=('professional_review', 'public_release'))
    p.add_argument('--self-test', action='store_true')
    a = p.parse_args()
    if a.self_test:
        self_test()
        return 0
    if not all((a.candidate, a.evidence, a.mode)):
        p.error('--candidate, --evidence and --mode are all mandatory except during --self-test')
    problems = verify(a.candidate, a.evidence, a.mode)
    if problems:
        print('BLOCKED — DO NOT PROMOTE/SHARE THIS CANDIDATE')
        for issue in problems:
            print(' - ' + issue)
        return 1
    print('EVIDENCE GATE PASSED — manual release approval and applicable clinical checks still required.')
    print('No files have been published by this script.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
