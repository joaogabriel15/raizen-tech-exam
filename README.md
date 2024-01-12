### Utilizando Docker Compose para Executar a Aplicação

#### Instruções de Uso:

0. **Crie o arquivo .env e adicione a chave da api:**

   URL do site pra gerar o token: [Link](https://home.openweathermap.org/api_keys)

   ```
   API_KEY = ''
   MONGO_INITDB_ROOT_USERNAME = 'root'
   MONGO_INITDB_ROOT_PASSWORD = 'example'
   MONGODB_URI = 'mongodb://mongodb:27017/'

   ```

   Isso criará e iniciará os contêineres em segundo plano.

1. **Criação e Inicialização dos Contêineres:**
   Execute o seguinte comando no diretório onde o `docker-compose.yml` está localizado:

   ```bash
   $ docker-compose up -d
   ```

   Isso criará e iniciará os contêineres em segundo plano.

2. **Parada e Remoção dos Contêineres:**
   Para parar e remover os contêineres, utilize:

   ```bash
   $ docker-compose down
   ```

3. **Acesso à Aplicação FastAPI:**
   A aplicação estará acessível em `http://127.0.0.1:8000`. Você pode acessar a documentação interativa em `http://127.0.0.1:8000/docs` para explorar e testar as rotas disponíveis.

4. **Acesso ao Banco de Dados MongoDB:**
   O serviço MongoDB estará acessível em `localhost:27017`.

#### Uso das Rotas Atualizado:

1. **Rota de Busca por Coordenadas:**
   - **Endpoint:** `POST /api/v1/search`
   - **Parâmetros de Exemplo:**
     ```json
     {
       "type_search": "coordinates",
       "coordinates": {"lat": 40.7128, "lon": -74.0060}
     }
     ```

2. **Rota de Busca por Query:**
   - **Endpoint:** `POST /api/v1/search`
   - **Parâmetros de Exemplo:**
     ```json
     {
       "type_search": "query",
       "query": {"city_name": "NomeCidade", "state_code": 123, "country_code": 456}
     }
     ```

3. **Rota de Busca por ID da Cidade:**
   - **Endpoint:** `POST /api/v1/search`
   - **Parâmetros de Exemplo:**
     ```json
     {
       "type_search": "id",
       "city_id": 2960
     }
     ```

4. **Rota de Busca Local:**
   - **Endpoint:** `GET /api/v1/search/local`
   - **Parâmetros de Exemplo:**
     ```json
     {
       "skip": 0,
       "limit": 10
     }
     ```
 
 ### Executando Testes com o Comando Pytest

Para executar os testes com o Pytest, utilize o seguinte comando:

```bash
docker-compose build

docker-compose run fastapi pytest -v
```

---
