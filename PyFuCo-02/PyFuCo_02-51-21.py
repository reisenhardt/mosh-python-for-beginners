def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":-)": "Sehr lustig, haha😂",
        ":-(": "I'm sorry, mate!😢",
        "ok": "You ✅, my old checker!"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
result = emoji_converter(message)
print(result)
