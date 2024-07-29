sentence  = input("Enter a sentence : ")

words_count = [(word, len(word)) for word in sentence.split()]
print(words_count)



