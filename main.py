import random
import string
mode = input("Choose random or word mode: ")
length = 8

if mode == "random":
    combine = random.sample(string.ascii_letters, 5) + random.sample(string.digits, 3)
    combine += random.choice(string.punctuation)
    password = "".join(random.sample(combine, length))
    print(password)

if mode == "word":
    with open("words.txt") as dictionary:
        word_choices = [word.strip() for word in dictionary]

    password_builder = list(random.choice(word_choices))
    index = random.randint(0, len(password_builder)-1)
    password_builder[index] = str.capitalize(password_builder[index])
    password_builder.append("".join(random.choice(string.digits) for i in range(length - 4)))
    password_builder.append(random.choice(string.punctuation))
    password = "".join(password_builder)
    print(password)
