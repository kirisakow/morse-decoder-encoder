import argparse
import re
import sys
from mde_constants.mde_constants import (
    LANGS, RE_DASH_CHARS, RE_DOT_CHARS, MORSE_KEYS)


def convert_to_ansi_morse(morse_str: str) -> str:
    for r in [RE_DASH_CHARS, RE_DOT_CHARS]:
        morse_str = re.sub(r['pattern'], r['by'], morse_str)
    return morse_str


def decode_from_morse(str_to_decode: str) -> dict:
    ret = {'str_to_decode': str_to_decode} | {lang: '' for lang in LANGS}
    for morse_chars in str_to_decode.split(' '):
        if morse_chars == '':
            for lang in LANGS:
                ret[lang] += ' '
            continue
        ansi_morse_chars = convert_to_ansi_morse(morse_chars)
        keys = [d for d in MORSE_KEYS if d['morse'] == ansi_morse_chars]
        if not keys:
            continue
        keys = keys[0]
        for lang in LANGS:
            key = keys.get(lang, keys.get('common', ''))
            ret[lang] += key[0]
    return ret


def encode_to_ansi_morse(str_to_encode: str) -> dict:
    ret = {'str_to_encode': str_to_encode, 'morse': ''}
    chars_to_encode = list(str_to_encode)
    for i, char_to_encode in enumerate(chars_to_encode):
        if char_to_encode == ' ':
            ret['morse'] += ' '
            continue
        for d in MORSE_KEYS:
            if any([char_to_encode.casefold() in v.casefold() for v in d.values()]):
                ret['morse'] += d['morse']
                break
        if i < len(chars_to_encode) - 1:
            ret['morse'] += ' '
    return ret


def read_from_stdin_and_print_to_stdout():
    MORSE_ACTIONS = {'decode': decode_from_morse, 'encode': encode_to_ansi_morse}
    DESCRIPTION = "Morse decoder & encoder."
    USAGE = f"""{DESCRIPTION}

python morse_decoder_encoder.py --decode "one (single, between quotes) Morse string to decode"

python morse_decoder_encoder.py --encode "one (single, between quotes) string to encode as Morse"

Run with -h (--help) option to print a complete help notice.
"""
    EPILOG = "See https://github.com/kirisakow/morse_decoder_encoder"
    parser = argparse.ArgumentParser(prog='morse_decoder_encoder.py', usage=USAGE, description=DESCRIPTION, epilog=EPILOG)
    parser.add_argument('--decode', help="decode Morse code", default=None, nargs=1, type=str)
    parser.add_argument('--encode', help="encode as Morse code", default=None, nargs=1, type=str)
    args = parser.parse_args()
    if not sys.argv[1:] or (args.decode is None and args.encode is None):
        sys.exit(USAGE)
    requested_action = sys.argv[1].lstrip('--')
    payload = args.__dict__.get(requested_action, '')
    if payload == '':
        sys.exit(USAGE)
    if isinstance(payload, list):
        payload = ' '.join(payload)
    result = MORSE_ACTIONS[requested_action](payload)
    print(f'{result!r}')


if __name__ == '__main__':
    read_from_stdin_and_print_to_stdout()
