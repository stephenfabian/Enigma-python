## About
This application is a tool that encrypts or decrypts a message by shifting the letters of a string.

## Info
 This is a project I created to learn the basics of Python.  There are a few things I would improve about this - including adding some additional test cases and refactoring some methods to utilize more complex ennumerables.  Since I have a background in Ruby there may be some Python conventional formatting aspects I'm overlooking as well. I spent around 5 hours creating this, and was excited to get this tool functioning in a new language! 

<h2>How to use the application</h2>

- Clone this repo

Example Encryption:

```bash
$ python3 encrypt.py message.txt encrypted_text.txt 

Encrypted text has been written to encrypted_text.txt, the key is 47762 and the date is 130223
```

Example Decryption:

```bash

$ python3 decrypt.py encrypted_text.txt decrypted_text.txt 47762 130223

Decrypted text has been written to decrypted_text.txt, the key is 47762 and the date is 130223

