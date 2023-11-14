""" from https://github.com/keithito/tacotron """

# Defines the set of symbols used in text input to the model.
_pad = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"

_punctuation_zh = '；：，。！？-“”《》、 —⑶～⑸⑾⑴·⑷①○⑤⑧〖〗－⑺□【】④'
_numbers = '1234567890'
_others = ''

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)
symbols_zh = [_pad] + list(_punctuation_zh) + list(_letters) + list(_numbers)

# Special symbol ids
SPACE_ID = symbols.index(" ")
