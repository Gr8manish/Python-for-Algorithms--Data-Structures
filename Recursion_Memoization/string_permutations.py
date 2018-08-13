# Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.
#
# For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#
# Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx'
# would return a list with 6 "versions" of 'xxx'


def permute(s):
    out = []
    if len(s) == 1:
        return s
    else:
        for index, letter in enumerate(s):
            for perm in permute(s[:index] + s[index+1:]):
                out += [letter + perm]
    return out


# Test Cases
print(permute('abc'))

# Output
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# Let's think about what the steps we need to take here are:
#
# 1.) Iterate through the initial string – e.g., ‘abc’.
#
# 2.) For each character in the initial string, set aside that character and get a list of all permutations of the string
# that’s left. So, for example, if the current iteration is on 'b', we’d want to find all the permutations of the string 'ac'.
#
# 3.) Once you have the list from step 2, add each element from that list to the character from the initial string, and
# append the result to our list of final results. So if we’re on 'b' and we’ve gotten the list ['ac', 'ca'], we’d add 'b' to those,
# resulting in 'bac' and 'bca', each of which we’d add to our final results.
#
# 4.) Return the list of final results.
