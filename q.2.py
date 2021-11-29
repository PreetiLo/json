import json

p={
    "name": "David", 
    "class": "I", 
    "age": 6
}
with open("text1.json","w") as file:
    p=json.dump(p,file,indent=6)
    print(p)
    
