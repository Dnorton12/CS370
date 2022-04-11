import hashlib
import string
import random


def weak_collision(num_passes):

    # Create variable to count number of test completed
    num_test = 0
    # Keep a running count to calc average at the end of the three passes
    total_count = 0

    # Main loop for running a certain number of passes
    for i in range(num_passes):
        # Used to keep track of the number of trials per pass
        trial = 0
        # Used to output our test number for display of the count of each pass
        num_test += 1

        # This is the string we will using to compare our non fixed string to during each trial.
        # We are using letters, numbers and symbols to generate this string.
        fixed_string = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(15))

        while True:

            # This is a variable string that will be randomly generated each pass and compared to the fixed string
            # define above. We are using letters, numbers and symbols to generate this string.
            non_fixed_string = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(15))

            # If they match before creating the hash then we move onto the next pass
            if fixed_string == non_fixed_string:
                continue

            else:

                # Generate hash for both strings
                hash_string_1 = hashlib.sha256(fixed_string.encode())
                hash_string_2 = hashlib.sha256(non_fixed_string.encode())

                # Turn hash into hex string
                hex_string_1 = hash_string_1.hexdigest()
                hex_string_2 = hash_string_2.hexdigest()

                # Increment trial number
                trial += 1

                # Compare first 24 bits of hex strings
                if hex_string_1[0:6] == hex_string_2[0:6]:
                    break

        # Print out our test number and number trials for the test
        print("Test %d took %d trials" % (num_test, trial))
        # Increment total count based on trials in the pass
        total_count += trial

    # Calc average based on total count and number of trials(tests) passed in
    average = total_count / num_passes
    # Print out the average of the test passes
    print("The average is: ", average)


if __name__ == '__main__':
    weak_collision(5)