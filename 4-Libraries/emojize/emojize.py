import emoji

user_input = input("Phrase you want to convert into emoji: ")
print(emoji.emojize(user_input, language="alias"))
