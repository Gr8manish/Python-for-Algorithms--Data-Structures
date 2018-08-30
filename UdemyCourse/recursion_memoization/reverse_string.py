# reverse a string using recursion

result = ""
def reverse_string(s, index):
    if index==len(s):
        return ""
    reverse_string(s,index+1)
    global result
    result += s[index]

def reverse(s):
    global result
    result = ""
    reverse_string(s,0)
    return result




# Test Case
print(reverse('hello world'))

# Output
# dlrow olleh