num = int(input())

words = []

for _ in range(num):
    word = input()
    if word in words:
        pass
    else:
        words.append(word)
    
words.sort(key = lambda x: (len(x), x))

for i in words:
    print(i)