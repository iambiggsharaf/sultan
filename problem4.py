s = "Salam Almaty. We are are from Dushanbe. Aga"

myDict = {}

def addEachWord(text):
    for i in text.split():
        i = i.lower()
        if len(i) in myDict:
            myDict[len(i)].append(i)
        else:
            myDict[len(i)] = [i]


addEachWord(s)

for i in sorted (myDict.keys()): 
     print("из " + str(i) + " " + str(len(myDict[i])))


for i in sorted (myDict.keys()): 
     print(myDict[i])