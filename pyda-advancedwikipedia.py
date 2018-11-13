import wikipedia
# Translate wikipedia data to GERMAN LANGUAGE
while True:
    input = input("Wiki Q: ")
    wikipedia.set_lang("de")
    print(wikipedia.summary(input))
