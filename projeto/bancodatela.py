import sqlite3

con = sqlite3.connect('bancoTela.db')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT ,
    senha TEXT
)
''')

def adicionar(nome, senha):
    cur = con.cursor()
    cur.execute(f"INSERT INTO usuarios (nome, senha) VALUES('"+nome+"', '"+senha+"')")
    con.commit()
    
def login(nome, senha):
    cur = con.cursor()
    cur.execute("SELECT * FROM usuarios")
    con.commit()
    usuario = cur.fetchall()
    if nome and senha in usuario:
        print('Login permitido')
    else:
        print('Não permitido')




