import letter

def test_letter_initialization():
  l = letter.Letter('a', 1)
  assert l is not None

def test_alphabet():
  l = letter.Letter('a', 1)
  result = l.alphabet()
  assert result == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def test_encrypt():
  char1 = letter.Letter('a', 1)
  char2 = letter.Letter('z', 2)
  char3 = letter.Letter('!', 2)
  result1 = char1.encrypt_character()
  result2 = char2.encrypt_character()
  result3 = char3.encrypt_character()
  assert result1 == 'b'
  assert result2 == 'a'
  assert result3 == '!'

def test_decrypt_letter():
  char1 = letter.Letter('b', 1)
  char2 = letter.Letter('a', 2)
  char3 = letter.Letter('!', 2)
  result1 = char1.decrypt_character()
  result2 = char2.decrypt_character()
  result3 = char3.decrypt_character()
  assert result1 == 'a'
  assert result2 == 'z'
  assert result3 == '!'

def test_valid_character():
   char1 = letter.Letter('b', 1)
   char2 = letter.Letter('!', 2)
   result1 = char1.valid_character()
   result2 = char2.valid_character()
   assert result1 == True
   assert result2 == False
