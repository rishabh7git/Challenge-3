myObj = {}    
myObj = input("Enter the object:\n")
print(myObj)
print("\n")
key = input("Enter the key:\n")
print(key)
print("\n")

def getObjVal(key,myObj):
    objKey = key
    tempObj = myObj
    arr = objKey.split('/')
    for k in arr:
        if k not in tempObj.keys():
            print("Key is not in the object")    
            print("None")
            return
        temp = k
        tempObj = tempObj.get(temp)
    
    print("Value as per input key:")
    print(str(tempObj))

getObjVal(key,myObj)