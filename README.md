# Criar ambiente virtual
python -m venv .venv

# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Atualizar requirements.txt
pip install <lib>
pip freeze > requirements.txt