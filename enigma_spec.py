import enigma

def test_enigma_initialization():
  e = enigma.Enigma("hello world", "02715", "040895")
  assert e.message == "hello world"
  assert e.key == "02715"
  assert e.date == "040895"

def test_encrypt():
  e = enigma.Enigma("Hello world", "02715", "040895")
  assert e.encrypt() == {
                         'encrypted_message': 'keder ohulw',
                         'key': '02715',
                         'date': '040895'
                         }

def test_decrypt():
  e = enigma.Enigma("keder ohulw", "02715", "040895")
  assert e.decrypt() == {
      'decrypted_message': "hello world",
                         'key': '02715',
                         'date': '040895'
                         }

def test_default_key():
  e = enigma.Enigma("hello world", "02715", "040895")
  result = e.default_key()
  assert isinstance(result, str), f"Expected str, but got {type(result).__name__}"
  assert len(str(result)) == 5

def test_default_date():
  e = enigma.Enigma("hello world", "02715", "040895")
  result = e.default_date()
  assert isinstance(result, str), f"Expected str, but got {type(result).__name__}"
  assert len(str(result)) == 5 or len(str(result)) == 6



