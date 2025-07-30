#imagem do docker
FROM python:3.11-slim    

# Definindo o diretório de trabalho  com base na minha pasta
WORKDIR /app

#copia todas as libs e dependências do projeto
COPY requirements.txt .

# instala as dependências(obs: estou instalando sem levar o cache para não ocupar espaço)       
RUN pip install --no-cache-dir -r requirements.txt  

# copia o código do projeto para dentro do container                            
COPY app/ ./app

#comando para rodar o servidor  

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
