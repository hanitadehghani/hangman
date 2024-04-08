import random

def put_corrects(word,lst):
    correct = ""
    for i in lst:
        for j in word:
            if i == j:
                correct += i
    finalCorrect = ""
    for p in word:
        if not p in correct:
            finalCorrect+="_"
        else:
            finalCorrect+=p
            
    return finalCorrect

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
    message += "_ " 

while True:
    print("guess the letter")
    print(message)
    userGuess = input("what is the {} word?".format(randomTitle["title"]))
  

    for j in userGuess:
        if j.upper() in randomItem:
       
            print(True)
        else:
            print(False)


