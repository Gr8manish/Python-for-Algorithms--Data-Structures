def rev_word(s):
    
    words = []
    spaces = [' ']
    length = len(s)
    end = start = 0
    while end < length:
        if s[end] in spaces:
            words.append(s[start:end])
            start = end
        end += 1
    words.append(s[start:end])
    return ' '.join(reversed(words))


# Test Cases
print(rev_word('Hi John,   are you ready to go?'))