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
print(randomTitle["title"])
print(randomItem)
