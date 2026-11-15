#!/usr/bin/env python3
"""Build landing pages and the identical released questionnaire for GitHub Pages."""
import argparse
import hashlib
import json
import re
from html import escape, unescape
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
PAGES={'en':('index.html',''),'lv':('lv.html','lv/'),'ru':('ru.html','ru/')}
LANGUAGE_NAMES={'en':'English','lv':'Latviešu','ru':'Русский'}
LANGUAGE_LABELS={'en':'Choose language','lv':'Izvēlieties valodu','ru':'Выберите язык'}

def questionnaire_bytes(require_verified_distribution=False):
 """Read only the allowlisted package HTML; publication also requires Drive parity."""
 folder=ROOT/'MH_Public_version'
 package=json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
 version=package.get('version','').split('-')[0]
 files=package.get('files',[])
 html_name='Mental_Health_Questionnaire_v'+version+'.html'
 pdf_name='Mental_Health_Questionnaire_Guide_v'+version+'.pdf'
 if (package.get('schema')!='questionnaire-review-package-v1'
     or package.get('source_dirty') is not False or not re.fullmatch(r'\d+\.\d+\.\d+',version)
     or not isinstance(files,list) or len(files)!=2
     or any(not isinstance(item,dict) for item in files)
     or {item.get('name') for item in files}!={html_name,pdf_name}):
  raise ValueError('Invalid released questionnaire package')
 path=folder/html_name
 if path.resolve().parent!=folder.resolve() or not path.is_file():
  raise ValueError('Questionnaire artifact is missing or outside the package')
 record=next(item for item in files if item['name']==html_name)
 payload=path.read_bytes()
 if len(payload)!=record.get('bytes') or hashlib.sha256(payload).hexdigest()!=record.get('sha256'):
  raise ValueError('Questionnaire artifact does not match its verified package')
 if require_verified_distribution:
  distribution=json.loads((ROOT/'project-manifest.json').read_text(encoding='utf-8')).get('review_distribution',{})
  expected={(item['name'],item.get('bytes'),item.get('sha256')) for item in files}
  actual={(item.get('name'),item.get('bytes'),item.get('sha256')) for item in distribution.get('files',[])}
  if (distribution.get('version')!=version or distribution.get('source_commit')!=package.get('source_commit')
      or not distribution.get('synchronization','').startswith('VERIFIED:') or expected!=actual):
   raise ValueError('Publish only after matching Drive distribution has been verified')
 return payload

def build(base_url, output, require_verified_distribution=False):
 url=urlsplit(base_url)
 if url.scheme!='https' or not url.hostname or url.query or url.fragment or url.username or url.password:
  raise ValueError('Publication URL must be absolute HTTPS without credentials, query or fragment')
 canonical=base_url.rstrip('/')+'/'
 questionnaire=questionnaire_bytes(require_verified_distribution)
 # Avoid leaking old output or repository files through a reused staging directory.
 output.mkdir(parents=True,exist_ok=False)
 source=ROOT/'docs/discovery-preview'
 shared_style=re.search(r'<style>.*?</style>',(source/'index.html').read_text(encoding='utf-8'),re.S).group()
 urls={locale:canonical+path for locale,(_,path) in PAGES.items()}
 banner='<p class="preview"><strong>Unpublished preview for owner review.</strong> This description page has not been deployed.</p>'
 for locale,(filename,path) in PAGES.items():
  text=(source/filename).read_text(encoding='utf-8').replace('<!-- SHARED_STYLE -->',shared_style)
  text=text.replace('__QUESTIONNAIRE_URL__',escape(canonical+'questionnaire/',quote=True))
  text=text.replace(banner,'').replace('  <!-- Unpublished preview. Add a canonical only after the owner approves the actual publication URL. -->\n','')
  title=unescape(re.search(r'<title>(.*?)</title>',text,re.S).group(1))
  description=unescape(re.search(r'<meta name="description" content="([^"]*)"',text).group(1))
  head='<link rel="canonical" href="'+escape(urls[locale],quote=True)+'">\n'
  head+=''.join('<link rel="alternate" hreflang="'+lang+'" href="'+escape(url,quote=True)+'">\n' for lang,url in urls.items())
  head+='<link rel="alternate" hreflang="x-default" href="'+escape(canonical,quote=True)+'">\n'
  for key,value in {'og:type':'website','og:title':title,'og:description':description,'og:url':urls[locale]}.items():
   head+='<meta property="'+key+'" content="'+escape(value,quote=True)+'">\n'
  text=text.replace('</head>',head+'</head>')
  navigation='<nav class="language-links" aria-label="'+LANGUAGE_LABELS[locale]+'"><ul>'
  navigation+=''.join('<li><a href="'+escape(url,quote=True)+'" lang="'+lang+'" hreflang="'+lang+'"'+(' aria-current="page"' if lang==locale else '')+'>'+LANGUAGE_NAMES[lang]+'</a></li>' for lang,url in urls.items())
  navigation+='</ul></nav>'
  text=text.replace('<header>','<header>\n'+navigation,1)
  destination=output/path/'index.html';destination.parent.mkdir(parents=True,exist_ok=True)
  destination.write_text(text,encoding='utf-8')
 (output/'questionnaire').mkdir()
 (output/'questionnaire/index.html').write_bytes(questionnaire)
 (output/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+escape(url)+'</loc></url>' for url in urls.values())+'</urlset>\n',encoding='utf-8')

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--base-url',required=True)
 parser.add_argument('--output',type=Path,required=True)
 parser.add_argument('--require-verified-distribution',action='store_true')
 args=parser.parse_args()
 build(args.base_url,args.output,args.require_verified_distribution)
