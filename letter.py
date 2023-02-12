class Letter:
  def __init__(self, character, shift):
    self.character = character.lower()
    self.shift = shift

  def alphabet(self):
    import string
    return list(string.ascii_lowercase + " ")

  def encrypt_character(self):
    alphabet = self.alphabet()
    character = self.character
    shift = self.shift
    if not self.valid_character():
      return self.character
    else:
      return alphabet[(alphabet.index(character) + shift) % len(alphabet)]

  def decrypt_character(self):
    alphabet = self.alphabet()
    character = self.character
    shift = self.shift
    if not self.valid_character():
      return self.character
    else:
      return alphabet[(alphabet.index(character) - shift) % len(alphabet)]

  def valid_character(self):
    return self.character in self.alphabet()
