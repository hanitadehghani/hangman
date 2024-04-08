import random



questions = [{
    'title': "food",
    "item" :["PIZZA","PASTA","SPAGHETTI"]}, 
{ 'title': "carModel",
    "item" : ["CADILLAC","TOYOTA","BMW"]},
    { 'title': "fruit",
    "item" : ["MANGO","APPLE","CHERRY"]}
]

randomTitle = random.choice(questions)
randomItem = random.choice(randomTitle["item"])
# print(randomTitle["title"])
# print(randomItem)
message = ""
for i in range(len(randomItem)):
    message += "_" + " "
while True:
    print("guess the letter")
    print(message)
    userGuess = input("what is the {} word?".format(randomTitle["title"]))
  

    for i in userGuess:
        if i.upper() in randomItem:
            print(True)
        else:
            print(False)


