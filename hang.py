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
message = ""
for i in range(len(randomItem)):
    message += "_" 
chosen_once=[]
lst = []
inCorrect = 0
x = True
while x:
    print("guess the letter")
    print(message)
    userGuess = input("what is the {} word?".format(randomTitle["title"]))
    if userGuess in chosen_once:
        print("Already chosen")
        print("try again")
        continue
    chosen_once.append(userGuess)
    print(chosen_once)
    
    for j in userGuess:
        if j.upper() in randomItem:
            lst.append(j.upper())
            word = put_corrects(randomItem,lst)
            message = word
            if word == randomItem:
                print("WELL DONE!")
                print(message)
                x = False
                break
   
            print(True)
            
        else:
            inCorrect += 1
            if inCorrect == 6:
                print("OHH... YOU LOST")
                x=False
                break
            print(False)
    
    
