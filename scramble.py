import letter

class Scramble:
  def __init__(self, message, key, date):
    self.message = message
    self.key = key
    self.date = date

  def keys(self):
    chars_aray = list(self.key)
    pairs = list(zip(chars_aray, chars_aray[1:]))
    joined_pairs = [f"{x}{y}" for x, y in pairs]
    return [int(num) for num in joined_pairs]

  def offsets(self):
    date_squared = int(self.date) * int(self.date)
    date_squared_array = list(str(date_squared))
    last_four_digits = [int(num) for num in date_squared_array[-4:]]
    return last_four_digits

  def shifts(self):
    result = []
    counter = 0
    for offset in self.offsets():
        result.append(self.keys()[counter] + offset)
        counter += 1
    return result

  def encrypt_message(self):
    counter = 0
    result = []
    chars_array = list(self.message)
    for char in chars_array:
      encrypted_character = letter.Letter(char, self.shifts()[counter]).encrypt_character()
      result.append(encrypted_character)
      counter +=1
      if counter > 3:
        counter = 0 
    return ''.join(result)

  def decrypt_message(self):
    counter = 0
    result = []
    chars_array = list(self.message)
    for char in chars_array:
      decrypted_character = letter.Letter(char, self.shifts()[counter]).decrypt_character()
      result.append(decrypted_character)
      counter +=1
      if counter > 3:
        counter = 0 
    return ''.join(result)


