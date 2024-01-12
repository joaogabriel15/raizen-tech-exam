from pymongo import MongoClient
from pymongo.collection import Collection

try:
    client = MongoClient(host='localhost', port=27017,  username='root',password='example')
    db = client['weather']
    
    if not isinstance(db.get_collection('weather'), Collection):
        colletion = db.create_collection('weather')
    else:
        colletion = db.get_collection('weather')
    
except Exception as e:
        print(f"Error in connect database: {e}")

