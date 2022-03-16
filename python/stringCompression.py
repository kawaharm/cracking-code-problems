# /*
# String Compression
# Implement a method to perform ....
# */

import unittest


def string_compression(string):
    # ### Doesnt work
    # str_array = []
    # count = 1

    # for i in range(len(str)):
    #     if str[i] != str[i+1] or (i+1) >= len(str):
    #         str_array.extend((str[i], count))
    #         count = 1
    #     else:
    #         count += 1

    str_array = []
    count = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i-1]:
            str_array.append(string[i-1] + str(count))
            count = 0
        count += 1

    # add last repeated character
    str_array.append(string[-1] + str(count))

    compressed_str = ''.join(str_array)
    print(compressed_str)

    return compressed_str if len(compressed_str) < len(string) else string


# // Test Cases
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
