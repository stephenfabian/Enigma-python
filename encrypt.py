import enigma
import sys

with open(sys.argv[1], "r") as file1:
  message = file1.read()

enigma_instance = enigma.Enigma(message)
enigma1 = enigma_instance.encrypt()

with open(sys.argv[2], "w") as file2:
    file2.write(enigma1["encrypted_message"])

print(f"Encrypted text has been written to {sys.argv[2]}, the key is {enigma_instance.key} and the date is {enigma_instance.date}")
