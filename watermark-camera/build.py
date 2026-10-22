"""Build the same demo as a single HTML file, with no external assets."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text(encoding='utf-8')
css = (root / 'style.css').read_text(encoding='utf-8')
js = (root / 'app.js').read_text(encoding='utf-8')
data = (root / 'design-data.json').read_text(encoding='utf-8')
json.loads(data)
html = html.replace('<link rel="stylesheet" href="style.css">', '<style>' + re.sub(r'</style', r'<\\/style', css, flags=re.I) + '</style>')
html = html.replace('<script id="design-data" type="application/json"></script>', '<script id="design-data" type="application/json">' + re.sub(r'</script', r'<\\/script', data, flags=re.I) + '</script>')
html = html.replace('<script src="app.js"></script>', '<script>' + re.sub(r'</script', r'<\\/script', js, flags=re.I) + '</script>')
out = root / '水印相机-交互演示.html'
out.write_text(html, encoding='utf-8')
print(f'{out}\n{out.stat().st_size:,} bytes; 22 embedded Figma scenes')
