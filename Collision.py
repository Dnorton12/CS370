import hashlib
import string
import random


def weak_collision(num_trials):

    num_test = 0
    total_count = 0

    for i in range(num_trials):
        trial = 0
        num_test += 1

        fixed_string = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(15))

        while True:

            non_fixed_string = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(15))

            if fixed_string == non_fixed_string:
                continue

            else:
                hash_string_1 = hashlib.sha256(fixed_string.encode())
                hash_string_2 = hashlib.sha256(non_fixed_string.encode())

                hex_string_1 = hash_string_1.hexdigest()
                hex_string_2 = hash_string_2.hexdigest()

                trial += 1

                if hex_string_1[0:6] == hex_string_2[0:6]:
                    break

        print("Test %d took %d trials" % (num_test, trial))
        total_count += trial

    average = total_count / num_trials
    print("The average is: ", average)


if __name__ == '__main__':
    weak_collision(3)