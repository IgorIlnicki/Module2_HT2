from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def input_error(func):                
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {str(e)}"
    return inner

uri = "mongodb+srv://user:user1@cluster0.g6s22by.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db=client.baza_cats
try:
    pass
    # db.cats.insert_one({
    #     "name": 'Barsik',
    #     "age": 3,
    #     "features": ['ходить в капці', 'дає себе гладити', 'рудий'],
    # })
    # db.cats.insert_one({
    #     "name": 'Murzik',
    #     "age": 1,
    #     "features": ['ходить в лоток', 'дає себе гладити', 'чорний'],
    # })
    # db.cats.insert_one({
    #     "name": 'Boris',
    #     "age": 12,
    #     "features": ['ходить в лоток', 'не дає себе гладити', 'білий'],
    # })
    # db.cats.update_one(
    # {"_id": ObjectId('65fd6348d26142c1d883ca81'),
    # "name": 'barsik1',
    # "age": 13,
    # "features": ['ходить в капці', 'дає себе гладити', 'рудий', 'їсть']
    # }) 
    # print(list(db.cats.find())) 
    # print(db.cats.delete_one({"_id": ObjectId("65fd6348d26142c1d883ca81")}))
    # print("Successfuli added")
except Exception as e:
    print(e)

@input_error
def list_all():
    try:
        data1 = list(db.cats.find())
        i = 0
        if len(data1) > 0:
            for value in data1:
                i +=1
                aa = value.get("name")
                bb = value.get("age")
                cc = value.get("features")
                string1 = ''
                ii = 0
                for el in cc:
                    ii +=1
                    string1 += str(ii) + ") " + el + " "
                print(f"{i:2}. Ім'я кота: {aa:10} Вік кота: {bb:2}  Особливості: {string1}")
        else:
            print("Список пустий")
    except Exception as e:
        print(e)

@input_error
def find_name(name):
    try:
        data1 = list(db.cats.find())
        kk = False
        i = 0
        for el in data1:
            if "name" in el:
                if name==el["name"]:
                    kk = True
                    bb = el.get("age")
                    cc = el.get("features")
                    print(f"Кота з іменем {name} знайдено:") 
                    string1 = ''
                    ii = 0 
                    for el2 in cc:
                        ii +=1
                        string1 += str(ii) + ") " + el2 + " "
                    print(f"Вік кота: {bb:2}  Особливості: {string1}")          
        if kk !=True:
            print(f"Кота з ім'ям {name} не знайдено.")
    except Exception as e:
        print(e)   

@input_error
def update_age(args):  # Міняємо вік кота
    try:
        name = args[0]
        age = int(args[1])
        if age > 0:
            data1 = list(db.cats.find())
            kk = False
            i = 0
            for el in data1:
                if "name" in el:
                    if name==el["name"]:
                        kk = True
                        bb = el.get("age")
                        print(f"Кота з іменем {name} знайдено:") 
                        print(f"Вік кота змінено з {bb} на {age}") 
                        # print(f"0   el = {el}")
                        el.update({"age":age})
                        # print(f"1   el = {el}")
                        # print(f"el.id = {el["_id"]}")  
                        # print(f"el.name = {el["name"]}") 
                        # print(f"el.age = {el["age"]}")   
                        db.cats.update_one(
                        {"_id": ObjectId(el["_id"])},
                        {"$set":
                        {"name": el["name"],
                        "age": el["age"],
                        "features": el["features"]
                        }
                        })
            if kk !=True:
                print(f"Кота з ім'ям {name} не знайдено.") 
        else:
            print(f"Невірно вказано вік кота.") 
    except Exception as e:
        print(e) 
@input_error
def update_feature(args):  #  міняємо характеристики кота
    try:
        name = args[0]
        feat = args[1]
        data1 = list(db.cats.find())
        kk = False
        i = 0
        for el in data1:
            if "name" in el:
                if name==el["name"]:
                    kk = True
                    bb = el.get("age")
                    print(f"Кота з іменем {name} знайдено:") 
                    print(f"Додана нова характеристика кота: {feat}") 
                    # print(f"0   el = {el}")
                    cc = []
                    cc = el.get("features")
                    # print(f"   cc = {cc}")
                    cc.append(feat)
                    el.update({"features":cc})
                    # print(f"1   el = {el}")
                    # print(f"el.id = {el["_id"]}")  
                    # print(f"el.name = {el["name"]}") 
                    # print(f"el.age = {el["age"]}")   
                    # print(f"el.feature = {el["features"]}") 
                    db.cats.update_one(
                        {"_id": ObjectId(el["_id"])},
                        {"$set":
                        {"name": el["name"],
                        "age": el["age"],
                        "features": el["features"]
                        }
                        })
        if kk !=True:
            print(f"Кота з ім'ям {name} не знайдено.")  
    except Exception as e:
        print(e) 

@input_error
def delete_name(name):
    try:
        data1 = list(db.cats.find())
        kk = False
        i = 0
        print(f"0 name = {name}")
        for el in data1:
            if "name" in el:
                if name==el["name"]:
                    kk = True
                    print(f"Кота з іменем {name} знайдено:") 
                    db.cats.delete_one(
                        {"_id": ObjectId(el["_id"])})
                    print(f"Кота з ім'ям {name} видалено.")          
        if kk !=True:
            print(f"Кота з ім'ям {name} не знайдено.")  
    except Exception as e:
        print(e)  

def parse_input(user_input): #ввод команди та аргументів
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Ласкаво просимо!")
    print("Формат команд:\n   list\n   find [name]\n   update_age [name] [new age]\n   update_feature [name] [new feature]")
    print("   delete_name [name]")
    while True: 
            user_input = input("Введіть команду: ")
            command, *args = parse_input(user_input)
            # print(f"000 comand = {command} args = {args}")
            if command in ["close", "exit"]:
                print("Допобачення!")
                break
            elif command == "list":
                list_all()
            elif command == "find":
                find_name(args[0])
            elif command == "update_age":
                update_age(args)
            elif command == "update_feature":
                update_feature(args)
            elif command == "delete_name":
                delete_name(args[0])
            else:
                print("Невірна команда!")
                break 

if __name__ == "__main__":
    main()