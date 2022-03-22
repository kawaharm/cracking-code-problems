# /*
# One Away
# There are three types of edits that can be performed on strings: insert a character,
# remove a character, and replace a character. Given two strings, write a function to check
# if they are one edit (or zero edits) away.
# */

def one_away(str1, str2):
    # // Return false if length differs by more than 1
    if abs(len(str1) - len(str2) > 1):
        return False

    hash = {}
    not_char = 0

    # // Add first string to hash table
    for i in range(len(str1)):
        print(str1[i])
        hash[str1[i]] = i

    for k in range(len(str2)):
        print(str2[k])
        if str2[k] in hash:
            not_char += 1
            if not_char > 1:
                return False

    return True


# // Test Cases
print(one_away('pale', 'ple'), 'TRUE')
print(one_away('pale', 'pales'), 'TRUE')
print(one_away('pale', 'bale'), 'TRUE')
print(one_away('pale', 'bake'), 'FALSE')

# NOT SOLVED
