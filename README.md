# 🚀 FastAPI Hello World + Monitoramento com Docker Compose

### 📂 Estrutura do Projeto
```
fastapi-hello/
│── app/
│   └── main.py
│── monitor_.py
│── Dockerfile
│── Dockerfile.monitor
│── docker-compose.yml
│── requirements.txt
│── .github/workflows/deploy.yml
│── README.md
```

---

## 🔥 O que o projeto faz
- Cria uma API simples com **FastAPI** retornando `"Hello World"`.
- Containeriza a aplicação usando **Docker**.
- Usa **Docker Compose** para orquestrar os serviços.
- Inclui um **serviço de monitoramento** que:
  - Faz health-check no endpoint `/`.
  - Monitora uso de CPU/RAM.
  - Gera logs e alerta em caso de falha.

---

## ▶️ Como rodar

### 1️⃣ Clone o repositório
```bash
git clone <https://github.com/gMoraes1/hello-word.git>
cd fastapi-hello
```

### 2️⃣ Suba os containers
```bash
docker compose up --build
```

Isso vai iniciar:

- **web** → API FastAPI, mostrando um print do seu iniciamento no terminal.  
- **monitor** → Script de monitoramento, que acessa o serviço web pelo hostname `web` e mostra prints do monitor iniciando e ciclos de monitoramento.

### 3️⃣ Acesse a API
- [http://localhost:8000](http://localhost:8000)  
- [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger)

### 4️⃣ Verifique os logs
Para ver os logs dos dois containers juntos:
```bash
docker compose logs -f
```

Para ver os logs do monitor separadamente (recomendado para monitoramento):
```bash
docker compose logs -f monitor
```

O monitor vai registrar mensagens no terminal e também em `monitor.log` dentro do container.

---

## 🧪 Testar localmente sem Docker
Se quiser rodar o monitor localmente (fora do container), instale as dependências:
```bash
pip install -r requirements.txt
```

E execute:
```bash
python3 monitor_.py
```

⚠️ **Lembre-se que nesse modo, o monitor deve usar `http://localhost:8000` para acessar a API, enquanto dentro do container o endereço é `http://web:8000`.**

---

## 📌 Pipeline CI/CD (GitHub Actions)
- O projeto inclui um workflow **GitHub Actions** (`.github/workflows/deploy.yml`).
- A cada **push na branch main**, o pipeline:
  - Builda o container.
  - Sobe a aplicação.
  - Faz health-check automático.
  - Mostra os logs e derruba o ambiente.

### 🔹 Disparar manualmente:
- Vá na aba **Actions** do repositório.
- Selecione o workflow *Build and Deploy FastAPI*.
- Clique em **Run workflow**.

---

## 📜 Exemplo de logs do monitor

```
[2025-07-29 21:32:01] 🚀 Iniciando monitoramento...
[2025-07-29 21:32:02] [OK] Endpoint http://web:8000 está respondendo.
[2025-07-29 21:32:02] [OK] CPU: 12.34%
[2025-07-29 21:32:02] [OK] RAM: 142.56 MB
[2025-07-29 21:32:07] [ALERTA] Falha ao acessar http://web:8000: Connection refused
```

---

## ✅ Requisitos
- Docker + Docker Compose v2  
- Git (para clonar o projeto)

---

## ✍️ Autor
Projeto criado para estudos de **FastAPI**, **Docker**, **Monitoramento com Python** e **CI/CD com GitHub Actions**.
