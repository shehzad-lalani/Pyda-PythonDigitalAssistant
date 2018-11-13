import wikipedia
import wolframalpha

while True:
    input = input("Q: ")

    try:
        #wolframalpha
        app_id = "P26XPU-EG6443ATGU"
        client = wolframalpha.Client(app_id)

        result = client.query(input)
        answer = next(result.results).text

        print(answer)

    except:
        #wikipedia

         wikipedia.set_lang("de")
        print(wikipedia.summary(input))
