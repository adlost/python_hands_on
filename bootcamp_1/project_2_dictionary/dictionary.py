import json

data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    else:
        print("Pugger you paw steps on wrong keys")


word = input("Enter the word you want to search: ")
output = translate(word)
print(output)
