word = input()
reverse_word_list = []

for i in range(1, len(word)-1, 1):
    for j in range(i+1, len(word), 1):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        reverse_word = a[::-1] + b[::-1] + c[::-1]
        reverse_word_list.append(reverse_word)

reverse_word_list = sorted(reverse_word_list)
print(reverse_word_list[0])