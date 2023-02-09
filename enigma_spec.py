import enigma

def test_enigma_initialization():
  e = enigma.Enigma()
  assert e is not None

def test_default_key():
  e = enigma.Enigma()
  result = e.default_key()
  assert isinstance(result, int), f"Expected int, but got {type(result).__name__}"
  assert len(str(result)) == 5

def test_default_date():
  e = enigma.Enigma()
  result = e.default_date()
  assert isinstance(result, int), f"Expected int, but got {type(result).__name__}"
  assert len(str(result)) == 5 or len(str(result)) == 6



