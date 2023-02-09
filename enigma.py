class Enigma:
    def default_key(self):
        import random
        random_number = random.randint(00000, 99999)
        return random_number

    def default_date(self):
        import datetime
        todays_date = int(datetime.datetime.now().strftime("%d%m%y"))
        # import ipdb; ipdb.set_trace()
        return todays_date

    # def encrypt(message, key=default_key, date=default_date):
   
    # def decrypt(ciphertext, key=default_key, date=default_date):

