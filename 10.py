
sentences = input()

words = [x for x in sentences.split()]

sets = set(words)

words = list(sets)
words.sort()


print(" ".join(words))