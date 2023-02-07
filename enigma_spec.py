import enigma

def test_default_key():
  result = enigma.default_key()
  assert isinstance(result, int), f"Expected int, but got {type(result).__name__}"
  assert len(str(result)) == 5

  
