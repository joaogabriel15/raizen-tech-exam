from pymongo import MongoClient
from pymongo.collection import Collection

try:
    # Tenta estabelecer uma conexão com o banco de dados MongoDB
    client = MongoClient('mongodb://mongodb:27017/',  username='root',password='example')
    # Seleciona o banco de dados 'weather'.
    db = client['weather']
    
    # Verifica se a coleção 'weather' já existe; se não existir, cria a coleção.
    if not isinstance(db.get_collection('weather'), Collection):
        colletion = db.create_collection('weather')
    else:
        colletion = db.get_collection('weather')
    
except Exception as e:
        # Em caso de erro na conexão, imprime uma mensagem de erro.
        print(f"Error in connect database: {e}")

