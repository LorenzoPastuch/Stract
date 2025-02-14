# Stract API

Este projeto é um servidor local em Python usando Flask que consome uma API de dados de anúncios e gera relatórios em formato CSV.

## 📌 Requisitos
- Python 3.8+
- `pip` instalado
- `git`instalado
- Conta no GitHub para clonar o repositório

## 🚀 Instalação

1. **Clone o repositório**
   ```sh
   git clone https://github.com/LorenzoPastuch/Stract.git
   cd Stract
   ```

2. **Crie e ative um ambiente virtual (recomendado)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
   ```

## ▶️ Como Executar

1. **Inicie o servidor Flask**
   ```sh
   python app.py
   ```

2. **Acesse a API via navegador ou ferramentas como Postman ou cURL**
   - Página inicial: [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/)
   - Relatório de uma plataforma específica: `http://127.0.0.1:5000/{plataforma}`
   - Resumo de uma plataforma: `http://127.0.0.1:5000/{plataforma}/resumo`
   - Relatório geral: [`http://127.0.0.1:5000/geral`](http://127.0.0.1:5000/geral)
   - Resumo geral: [`http://127.0.0.1:5000/geral/resumo`](http://127.0.0.1:5000/geral/resumo)

## 📂 Estrutura do Projeto
```
Stract/
│-- app.py              # Código principal da API Flask
│-- requirements.txt    # Lista de dependências do projeto
│-- README.md           # Documentação do projeto
```

## 📄 Formato dos Relatórios
Os endpoints retornam arquivos CSV contendo as informações dos anúncios.
- Os arquivos `geral` incluem dados de todas as plataformas.
- Os arquivos `resumo` consolidam os dados por plataforma ou conta.
- Para o Google Analytics, o campo "Cost per Click" é calculado como `spend / clicks`.
