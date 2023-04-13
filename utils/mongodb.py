import pymongo


def main2():
    usr = "pkubon2"
    pwd = ""
    with open('mongo_pwd.txt') as f:
        pwd = f.readlines()

    client = pymongo.MongoClient(
        f"mongodb://{usr}:{pwd}@ac-1tltdjz-shard-00-00.kdizqwu.mongodb.net:27017,"
        f"ac-1tltdjz-shard-00-01.kdizqwu.mongodb.net:27017,"
        f"ac-1tltdjz-shard-00-02.kdizqwu.mongodb.net:27017/?"
        f"ssl=true&replicaSet=atlas-rba8e3-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = client.test
    mydb = client["allegro_database"]
    mycol = mydb["categories_collection"]

    mydict = {"name": "John", "address": "Highway 37"}
    x = mycol.insert_one(mydict)
