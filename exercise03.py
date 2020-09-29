def reversed_string(word):
    return ''.join(reversed(word))

word = input("Digite alguma palavra: ")
reversed_word = reversed_string(word)
print("A palavra invertida é:",reversed_word)
