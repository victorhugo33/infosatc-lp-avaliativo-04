def is_the_same_reversed(word,word2):
    reversed_word = ''.join(reversed(word2))
    if word == reversed_word:
        return True
    else:
        return False

print("\nSerá solicitado duas palavras e será verificado se uma é o inverso da outra")
word = input("Digite alguma palavra: ")
word2 = input("Digite outra palavra: ")

if is_the_same_reversed(word,word2):
    print("São inverso")
else:
    print("Não são o inverso")
