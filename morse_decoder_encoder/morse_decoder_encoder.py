import re
from morse_decoder_encoder_constants import (
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
