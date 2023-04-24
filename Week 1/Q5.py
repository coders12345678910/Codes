def num_vowels(text):

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for x in text:
        if x.lower() in vowels:
            count +=1

    print(f"The sum of vowels in", text, "is", count)

num_vowels('paranthesis')
