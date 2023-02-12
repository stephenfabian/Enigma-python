import scramble

def test_scramble_initialization():
  instance = scramble.Scramble("Hello World", "12715", "120223")
  assert instance is not None

def test_keys():
  instance = scramble.Scramble("Hello World", "12715", "120223")
  result = instance.keys()
  assert result == [12, 27, 71, 15]

def test_offsets():
  instance = scramble.Scramble("Hello World", "12715", "120223")
  result = instance.offsets()
  assert result == [9, 7, 2, 9]

def test_shifts():
  instance = scramble.Scramble("Hello World", "12715", "120223")
  result = instance.shifts()
  assert result == [21, 34, 73, 24]

def test_encrypt_message():
  instance = scramble.Scramble("Hello World", "02715", "040895")
  result = instance.encrypt_message()
  assert result == "keder ohulw"

def test_decrypt_message():
  instance = scramble.Scramble("keder ohulw", "02715", "040895")
  result = instance.decrypt_message()
  assert result == "hello world"


