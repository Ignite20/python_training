pyg = 'ay'
vowels = ["a", "e", "i", "o", "u"]
original = input('Enter a word:')

words = original.split(" ")
newPhrase = ""


for position in range(0, len(words)):
    currWord = words[position].lower()
    if len(currWord) > 0 and currWord.isalpha():
        word = currWord.lower()
        new_word = ""
        if not currWord[0:1] in vowels and currWord[1:2] in vowels:
            first = word[0]
            new_word = word[1:len(word)] + first + pyg
        elif not currWord[0:1] in vowels and not currWord[1:2] in vowels:
            first = word[0:2]
            new_word = word[2:len(word)] + first + pyg
        elif currWord[0:1] in vowels:
            new_word = word + pyg
        newPhrase += new_word + " "
    else:
        print('empty')

print(newPhrase)
