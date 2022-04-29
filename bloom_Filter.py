# These are the imports used in my bloom filter
import hashlib
import math
import sys
from bitarray import bitarray


# Function to add a new dictionary item to the bloom filter
# Passwords will be compared against what is place in the bitarray
def add(add_word, bloom, bit_arr_size, num_hashes):

    # Run through a loop for the number of hashes determined
    # This program uses the SHA256 encryption types
    for i in range(num_hashes):

        # Initialize the hash value
        digest = hashlib.sha256(add_word.encode('windows-1252'))

        # Get the index and convert hex hash value to decimal
        index = int(digest.hexdigest(), 16) % bit_arr_size

        # Set index in bit array to 1/True
        bloom[index] = 1



# Function to check passwords against hashed dictionary items in bit array
def check(add_word, bloom, bit_arr_size, num_hashes):

    # Run through a loop for the number of hashes determined
    # Check will compare against the same hash type as the add function - SHA256
    for i in range(num_hashes):

        # Initialize the hash value for the password we are using to compare
        digest = hashlib.sha256(add_word.encode('windows-1252'))

        # Get the index and convert hex hash value to decimal
        index = int(digest.hexdigest(), 16) % bit_arr_size

        # If bit is 0(False) then item isn't in bloom filter and return False
        if bloom[index] == 1:
            return True
        elif bloom[index] == 0:
            continue
    return False


# Function is used to calculate the size of the bit array we need to use
def get_size(n, p):
    m = -(n * math.log(p)) / (math.log(2)**2)
    return int(m)


# Function is used to calculate the the number of hashes we need to use
def get_hash_number(m, n):
    k = (m/n) * math.log(2)
    return int(k)


if __name__ == '__main__':

    # User sets false probability percent, which is used to help calc size of bit array
    probability = 0.05

    # System args used when running program from the command line
    args = sys.argv
    # Dictionary file used to add indexes to bit array
    dictionary = args[1]
    # File used to compare against the bit array
    inputfile = args[2]
    # File which outputs the results of the bloom filter
    outfile = args[3]

    # This block of code opens the dictionary file, reads it, strips the spaces and new line
    # characters off and counts the number of items in the file which is then passed into get_size
    numberWords = 0
    f = open(dictionary, 'r', encoding='windows-1252')
    words = f.read()
    words = words.strip()
    words = words.split("\n")
    numberWords += len(words)

    # This block of code opens the input file(passwords), reads it, strips the spaces and new line
    # characters off. This is used with the check function to compare against the bit array
    f = open(inputfile, 'r', encoding='windows-1252')
    passwords = f.read()
    passwords = passwords.strip()
    passwords = passwords.split("\n")

    # Get the size of our bit array
    bit_array_size = get_size(numberWords, probability)

    # Set up the bloom filter based on size we calculated
    bloomFilter = bitarray(bit_array_size)

    # Set all indexes to 0(False)
    bloomFilter.setall(0)

    # Calculate the number of hashes we need
    numHashes = get_hash_number(bit_array_size, numberWords)

    # This will just print out the size of the array we calculated, what our set false probability percent is and
    # the number of hashes we calculated
    print("Size of bit array:{}".format(bit_array_size))
    print("False positive Probability:{}".format(probability))
    print("Number of hash functions:{}".format(numHashes))

    # Open our output file for writing results
    f = open(outfile, 'w+')

    # Run through the dictionary and add the line items to the bit array by calling the add method
    for item in words:
        add(item, bloomFilter, bit_array_size, numHashes)

    # Check our password line items against the bit array
    for word in passwords:
        # local variable used to store the results from the check call
        passCheck = check(word, bloomFilter, bit_array_size, numHashes)

        # Checks the value returned fromo the call, if True states it may be present
        if passCheck is True:
            f.write("'{}' is a maybe present!\n".format(word))

        # Otherwise it returns False and it is not present
        else:
            f.write("'{}' is not present!\n".format(word))