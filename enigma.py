def default_key():
    import random
    random_number = random.randint(00000, 99999)
    return random_number
    # import ipdb; ipdb.set_trace()

def default_date():
    import datetiem
    today = datetime.datetime.now().strftime("%d%m%y")
