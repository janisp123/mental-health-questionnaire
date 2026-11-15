#!/usr/bin/env python3
"""Build a page-only GitHub Pages artifact using its configured publication URL."""
import argparse
import re
from html import escape, unescape
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
PAGES={'en':('index.html',''),'lv':('lv.html','lv/'),'ru':('ru.html','ru/')}
LANGUAGE_NAMES={'en':'English','lv':'Latviešu','ru':'Русский'}
LANGUAGE_LABELS={'en':'Choose language','lv':'Izvēlieties valodu','ru':'Выберите язык'}

def build(base_url, output):
 url=urlsplit(base_url)
 if url.scheme!='https' or not url.hostname or url.query or url.fragment or url.username or url.password:
  raise ValueError('Publication URL must be absolute HTTPS without credentials, query or fragment')
 canonical=base_url.rstrip('/')+'/'
 # Avoid leaking old output or repository files through a reused staging directory.
 output.mkdir(parents=True,exist_ok=False)
 source=ROOT/'docs/discovery-preview'
 shared_style=re.search(r'<style>.*?</style>',(source/'index.html').read_text(encoding='utf-8'),re.S).group()
 urls={locale:canonical+path for locale,(_,path) in PAGES.items()}
 banner='<p class="preview"><strong>Unpublished preview for owner review.</strong> This description page has not been deployed.</p>'
 for locale,(filename,path) in PAGES.items():
  text=(source/filename).read_text(encoding='utf-8').replace('<!-- SHARED_STYLE -->',shared_style)
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
 (output/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+escape(url)+'</loc></url>' for url in urls.values())+'</urlset>\n',encoding='utf-8')

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--base-url',required=True)
 parser.add_argument('--output',type=Path,required=True)
 args=parser.parse_args()
 build(args.base_url,args.output)
