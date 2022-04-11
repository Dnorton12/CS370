from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# plaintext statement
plaintext = bytearray("This is a top secret.", encoding='utf-8')
# ciphertext value
ciphertext = bytearray.fromhex("8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9")
# iv value
iv = b'\x00' * 16

# open document which has all english words less than 16 characters
with open('./words.txt') as f:
    # read each line of txt file
    keys = f.readlines()

# loop to go through each key in the file to see if we find a match
for k in keys:
    # remove the new line character from each line
    k = k.rstrip('\n')
    # check if we the word is less than 16 characters, if it is we pad with spaces
    if len(k) <= 16:
        key = k + ' '*(16-len(k))
        # encrypt the plaintext to see if we match the ciphertext
        cipher = AES.new(key=bytearray(key, encoding='utf-8'), mode=AES.MODE_CBC, iv=iv)
        guess = cipher.encrypt(pad(plaintext, 16))
        if guess == ciphertext:
            print("The key is:", key)
            exit(0)

print("cannot find the key!")