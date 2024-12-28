# Encode a message
import string


chars = " " + string.punctuation + string.digits + string.ascii_letters
char = list(chars)
key = ['E', '+', '^', ' ', '4', '0', 'p', 'K', 'o', 'J', '(', 'I', 'u',
       'n', 'w', ':', '?', '<', '=', "'", 'B', '|', '5', 'Z', '#', 'm',
       'v', 'T', 'r', ',', '-', '{', 's', 'F', 'W', '2', '7', '\\', 'X',
       '`', '$', '1', '9', '}', 'h', 'V', 'G', 'a', 'g', 'R', '[', '8',
       'l', '*', 'C', '.', 'S', ']', 'e', 'z', '%', ';', '6', '"', 'Y',
       'y', 'P', 'i', 't', ')', 'c', 'b', 'f', '>', '!', 'U', 'd', '/',
       'x', 'q', '&', '~', 'O', '_', 'N', 'A', 'D', 'L', 'M', 'k', 'Q',
       '@', 'j', 'H', '3']

# key = char.copy()
# random.shuffle(key)



# Encryption
plain_text = input("Enter message to encrypt: ")
cypher_text = " "

for letter in plain_text:
    index = char.index(letter)
    cypher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cypher_text}")

# Decryption
cypher_text = input("Enter message to decode: ")
plain_text = " "

for letter in cypher_text:
    index = key.index(letter)
    plain_text += char[index]
    
print(f"Encrypted message: {cypher_text}")
print(f"Original message: {plain_text}")


