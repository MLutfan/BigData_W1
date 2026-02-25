from pymongo import MongoClient

uri = "mongodb+srv://free_for_all:2yduFGKfMMkV0wcq@wse230104040129.cvwga4m.mongodb.net/?appName=WSE230104040129"

client = MongoClient(uri)
print("Koneksi berhasil!")
print(client.list_database_names())