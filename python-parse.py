#!/usr/bin/env python3

word_count = dict()

def most_common_words(num=10):
    sorted_words = sorted(word_count, key=word_count.get, reverse=True)
    return sorted_words[:num]

with open('lorem') as f:
    for line in f:
        words = line.split()
        prepared_words = [w for w in words]
        for w in prepared_words:
            word_count[w] = 1 if w not in word_count else word_count[w] + 1


to_print = '\n'.join(most_common_words(40))

print('Most frequent words: ')
print(to_print)
