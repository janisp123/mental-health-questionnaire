#!/usr/bin/env python3
"""Build a page-only GitHub Pages artifact using its configured publication URL."""
import argparse
from html import escape
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]

def build(base_url, output):
 url=urlsplit(base_url)
 if url.scheme!='https' or not url.hostname or url.query or url.fragment or url.username or url.password:
  raise ValueError('Publication URL must be absolute HTTPS without credentials, query or fragment')
 canonical=base_url.rstrip('/')+'/'
 # Avoid leaking old output or repository files through a reused staging directory.
 output.mkdir(parents=True,exist_ok=False)
 text=(ROOT/'docs/discovery-preview/index.html').read_text(encoding='utf-8')
 banner='<p class="preview"><strong>Unpublished preview for owner review.</strong> This description page has not been deployed.</p>'
 text=text.replace(banner,'').replace('  <!-- Unpublished preview. Add a canonical only after the owner approves the actual publication URL. -->\n','')
 text=text.replace('</head>','  <link rel="canonical" href="'+escape(canonical,quote=True)+'">\n</head>')
 (output/'index.html').write_text(text,encoding='utf-8')
 (output/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+escape(canonical)+'</loc></url></urlset>\n',encoding='utf-8')

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--base-url',required=True)
 parser.add_argument('--output',type=Path,required=True)
 args=parser.parse_args()
 build(args.base_url,args.output)
