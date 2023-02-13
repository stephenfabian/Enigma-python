import enigma
import sys

with open(sys.argv[1], "r") as file1:
  encrypted_message = file1.read()

enigma_instance = enigma.Enigma(encrypted_message, sys.argv[3], sys.argv[4])
enigma1 = enigma_instance.decrypt()

with open(sys.argv[2], "w") as file2:
    file2.write(enigma1["decrypted_message"])

print(
    f"Decrypted text has been written to {sys.argv[2]}, the key is {enigma_instance.key} and the date is {enigma_instance.date}")
