def compress(string):

    length = len(string)

    if length==0:
        return ""

    if length==1:
        return string+"1"

    result = ""
    curr_char = string[0]
    i = 1
    cnt = 1
    while i < len(string):
        if curr_char == string[i]:
            cnt += 1
        else:
            result += curr_char+str(cnt)
            cnt = 1
            curr_char = string[i]
        i += 1
    result += curr_char + str(cnt)
    return result


# Test Cases
print(compress('AAAAABBBBCCCC'))
print(compress('AABBCC'))
print(compress('AAABCCDDDDD'))

# Output
# A5B4C4
# A2B2C2
# A3B1C2D5