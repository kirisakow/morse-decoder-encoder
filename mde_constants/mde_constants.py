import json
import os

LANGS = ['cyrillic', 'latin']

RE_DASH_CHARS = {'pattern': r'[−—–_]', 'by': '-'}

RE_DOT_CHARS = {'pattern': r'[⋅•*]', 'by': '.'}

MORSE_KEYS = json.load(
    open(os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../assets/morse_keys.json')
    ))
)
