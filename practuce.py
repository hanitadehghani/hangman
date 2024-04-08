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



w = "APPLE"
l = ["P","E"]
print(put_corrects(w,l))