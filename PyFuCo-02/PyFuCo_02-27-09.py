message = input(">")
words = message.split(" ")
emojis = {
    ":-)": "Sehr lustig, haha😂",
    ":-(": "I'm sorry, mate!😢",
    "ok": "You ✅, my old checker!"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

# Good morning :)