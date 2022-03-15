#! /usr/bin/python3

#we will convert all vowels into X

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #same function as if letter in "AEIOUaeiou"
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase you want to translate: ")))
