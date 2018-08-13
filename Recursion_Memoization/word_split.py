# Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine
# if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will
# only contain words found in the dictionary if it is completely splittable.

word = ""
list_of_words = []
output = []
length = 0;


def word_split(word1,list_of_words1):
    global list_of_words,word,length,output
    list_of_words = list_of_words1
    word = word1
    length = len(word)
    output = []
    split_the_word(0,0)
    return output


def split_the_word(start, end):
    if end > length:
        return

    if word[start:end] in list_of_words:
        print(word[start:end])
        output.append(word[start:end])
        start = end

    end += 1
    split_the_word(start,end)


print(word_split('themanran', ['the', 'ran', 'man']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
