# Morse decoder & encoder

It is available as both a library and a self-hosted [web service](https://github.com/kirisakow/api-py).

### Decode Morse
```py
from morse_decoder_encoder import decode_from_morse
from pprint import pprint

test_data = {
  'morse': '••• −•− •− −−•• •− −• −• −−− •  •• ••• −−−• • −−•• •− • − •−•−•−  −• •− •−−• •• ••• •− −• −• −−− •  −−− ••• − •− • − ••• •−•−',
  'cyrillic': 'СКАЗАННОЕ ИСЧЕЗАЕТ, НАПИСАННОЕ ОСТАЕТСЯ'
}
morse_str_to_decode = test_data['morse']
expected_decoded_cyrillic = test_data['cyrillic']
actual_decoded = decode_from_morse(morse_str_to_decode)
assert actual_decoded['cyrillic'] == expected_decoded_cyrillic
pprint(actual_decoded)
```
Result:
```
{
  'str_to_decode': '••• −•− •− −−•• •− −• −• −−− •  •• ••• −−−• • −−•• •− • − •−•−•−  −• •− •−−• •• ••• •− −• −• −−− •  −−− ••• − •− • − ••• •−•−',
  'cyrillic': 'СКАЗАННОЕ ИСЧЕЗАЕТ, НАПИСАННОЕ ОСТАЕТСЯ',
  'latin': 'SKAZANNOE ISÖEZAET, NAPISANNOE OSTAETSÄ'
}
```
### Encode to Morse
```py
from morse_decoder_encoder import encode_to_ansi_morse, convert_to_ansi_morse
from pprint import pprint

test_data = {
  'morse': '••• −•− •− −−•• •− −• −• −−− •  •• ••• −−−• • −−•• •− • − •−•−•−  −• •− •−−• •• ••• •− −• −• −−− •  −−− ••• − •− • − ••• •−•−',
  'cyrillic': 'СКАЗАННОЕ ИСЧЕЗАЕТ, НАПИСАННОЕ ОСТАЕТСЯ'
}
cyrillic_str_to_encode = test_data['cyrillic']
expected_morse = test_data['morse']
actual_result = encode_to_ansi_morse(cyrillic_str_to_encode)
assert convert_to_ansi_morse(expected_morse) == actual_result['morse']
pprint(actual_result)
```
Result:
```
{
  'str_to_encode': 'СКАЗАННОЕ ИСЧЕЗАЕТ, НАПИСАННОЕ ОСТАЕТСЯ',
  'morse': '... -.- .- --.. .- -. -. --- .  .. ... ---. . --.. .- . - .-.-.-  -. .- .--. .. ... .- -. -. --- .  --- ... - .- . - ... .-.-'
}
```

### Sources

* Morse code map for latin and cyrillic characters:
  * https://en.wikipedia.org/wiki/Russian_Morse_code
