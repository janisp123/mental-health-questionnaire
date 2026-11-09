import unittest

from workspace import check_pack, source_digest


class PackChecks(unittest.TestCase):
    def setUp(self):
        self.source = {
            "Q01": {"title": "Kā jūtaties?", "time": "", "choices": {"A": "Labi", "B": "Slikti"}},
            "Q02": {"title": "Kā gulējāt?", "time": "Vakar.", "choices": {"A": "Labi"}, "help": "Izvēlieties atbildi."},
        }
        self.translation = {
            "title": "Як Ви почуваєтеся?",
            "time": "",
            "choices": {"A": "Добре", "B": "Погано"},
        }
        self.pack = {"source_sha256": source_digest(self.source), "questions": {"Q01": self.translation}}

    def test_partial_pack_requires_full_coverage_only_on_completion(self):
        self.assertEqual(check_pack(self.source, self.pack), 1)
        with self.assertRaisesRegex(ValueError, "Q02"):
            check_pack(self.source, self.pack, complete=True)

    def test_wrong_answer_codes_and_empty_labels_are_rejected(self):
        self.translation["choices"] = {"A": "Добре", "C": "Погано"}
        with self.assertRaisesRegex(ValueError, "answer codes"):
            check_pack(self.source, self.pack)
        self.translation["choices"] = {"A": "Добре", "B": " "}
        with self.assertRaisesRegex(ValueError, "Q01.choices.B"):
            check_pack(self.source, self.pack)

    def test_missing_help_and_unknown_question_are_rejected(self):
        self.pack["questions"]["Q02"] = {"title": "Як Ви спали?", "time": "Учора.", "choices": {"A": "Добре"}}
        with self.assertRaisesRegex(ValueError, "Q02.*fields"):
            check_pack(self.source, self.pack)
        self.pack["questions"] = {"Q03": self.translation}
        with self.assertRaisesRegex(ValueError, "Q03"):
            check_pack(self.source, self.pack)

    def test_changed_latvian_source_is_detected(self):
        self.source["Q01"]["title"] = "Kā jūtaties šodien?"
        with self.assertRaisesRegex(ValueError, "source hash"):
            check_pack(self.source, self.pack)


if __name__ == "__main__":
    unittest.main()
