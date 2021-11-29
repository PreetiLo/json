# Q.9 Apki pass ek shopping name ki ek dictionary hai
import json
j={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

with open('shopping.json','w') as f:
    json.dump(j,f,indent=3)