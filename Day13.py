text = input("Enter your statement:")
for word in text.split(' '):
        if word.isupper():
            print(word)
