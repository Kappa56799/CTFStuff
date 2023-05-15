# Description: This script will decrypt the message.txt file and print the flag (inverse of mod 41)
import string
file = open("message.txt", "r")
number_list = file.read()
numbers = number_list.split()

key = string.ascii_lowercase
key += "0123456789_"

mod = 41

print(key)

text = ""

for n in numbers:
    x = pow(int(n), -1, mod) 
    text += key[x-1]
print(f"picoCTF{{{text}}}")
