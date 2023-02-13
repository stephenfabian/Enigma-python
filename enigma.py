import scramble

class Enigma:
    def __init__(self, message, key=None, date=None):
        self.message = message
        if key is None:
            self.key = self.default_key()
        else:
            self.key = key
        if date is None:
            self.date = self.default_date()
        else:
            self.date = date

    def encrypt(self):
        return {
                "encrypted_message": scramble.Scramble(self.message, self.key, self.date).encrypt_message(), 
                "key": self.key, 
                "date": self.date
                }

    def decrypt(self):
        return {
                "decrypted_message": scramble.Scramble(self.message, self.key, self.date).decrypt_message(), 
                "key": self.key, 
                "date": self.date
                }

    def default_key(self):
        import random
        random_number = str(random.randint(00000, 99999))
        return random_number

    def default_date(self):
        import datetime
        todays_date = datetime.datetime.now().strftime("%d%m%y")
        return todays_date


        # import ipdb; ipdb.set_trace()