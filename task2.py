import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

#reversing the words 
reversePhrase = randomPhrase[::-1]

# output for random words
print("Words in normal Display: ")
print(randomPhrase)
print("-" * 30)
# output for reverse of random words 
print("Words in reverse Display: ")
print (reversePhrase)
