import hashlib
import string
import random


def strong_collision(num_passes):

    # Table to hold values we've generated and then need to looked at
    lookup_table = {}
    # Create variable to count number of test completed
    num_test = 0
    # Keep a running count to calc average at the end of the three passes
    total_count = 0

    # Main loop for running a certain number of passes
    for i in range(num_passes):

        # Used to keep track of the number of trials per pass
        trial = 0
        # So we know which test number we are on
        num_test += 1

        while True:
            # Create a random string of letter, numbers and punc symbols to store in a string
            random_string = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(15))
            # Hash the random string we just generated
            hash_string_1 = hashlib.sha256(random_string.encode())
            # Turn hash string into a hex string
            hex_string_1 = hash_string_1.hexdigest()
            # Grab first 24 bits of the hex string to use for comparison
            comp_string = hex_string_1[0:6]
            # Compare new value with values in the lookup table
            if comp_string in lookup_table:
                # Add one to count to break out of loop
                trial += 1
                break
            else:
                # Add one to count and add value to lookup table
                trial += 1
                lookup_table[comp_string] = random_string

        # Print out our test number and number trials for the test
        print("Test %d took %d trials" % (num_test, trial))
        # Increment total count based on trials in the pass
        total_count += trial

    # Calc average based on total count and number of trials(tests) passed in
    average = total_count / num_passes
    # Print out the average of the test passes
    print("The average is: ", average)


if __name__ == '__main__':
    strong_collision(100)