import pytest
from morse_decoder_encoder.morse_decoder_encoder import (
    convert_to_ansi_morse,
    decode_from_morse,
    encode_to_ansi_morse,
)


test_data = {
    'morse': '••• −•− •− −−•• •− −• −• −−− •  •• ••• −−−• • −−•• •− • − •−•−•−  −• •− •−−• •• ••• •− −• −• −−− •  −−− ••• − •− • − ••• •−•−',
    'cyrillic': 'СКАЗАННОЕ ИСЧЕЗАЕТ, НАПИСАННОЕ ОСТАЕТСЯ'
}


def test_morse_to_cyrillic():
    morse_str_to_decode = test_data['morse']
    actual_decoded = decode_from_morse(morse_str_to_decode)
    expected_decoded_cyrillic = test_data['cyrillic']
    assert expected_decoded_cyrillic == actual_decoded['cyrillic']


def test_cyrillic_to_morse():
    cyrillic_str_to_encode = test_data['cyrillic']
    actual_morse = encode_to_ansi_morse(cyrillic_str_to_encode)['morse']
    expected_morse = convert_to_ansi_morse(test_data['morse'])
    assert expected_morse == actual_morse
