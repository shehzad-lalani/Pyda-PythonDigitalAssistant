import wolframalpha

input = input("Question: ")
app_id = "P26XPU-EG6443ATGU"
client = wolframalpha.Client(app_id)

result = client.query(input)
answer = next(result.results).text

print(answer)
