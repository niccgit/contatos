import sqlite3

def conexao_banco():

    conexao = sqlite3.connect("contatos.db")
    cursor = conexao.cursor()
    
    sql = '''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    )'''
    cursor.execute(sql)
    conexao.commit()
    return conexao

def adicionar_contato(nome, telefone, email):
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)'''
    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()
    conexao.close()

def listar_contatos():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''SELECT * FROM contatos'''
    cursor.execute(sql)
    contatos = cursor.fetchall()
    conexao.close()
    if len(contatos) == 0:
        print("Nenhum contato encontrado.")
    else:
        print("### LISTA DE CONTATOS ###")
        print(f"{'ID':<5} | {'Nome':<20} | {'Telefone':<15} | {'Email':<30}")
        print('-' * 80)
        for contato in contatos:
            print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")
        
def buscar_contato():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''SELECT * FROM contatos WHERE nome LIKE ?'''
    cursor.execute(sql, ('%' + input("Digite o nome do contato: ") + '%',))
    contatos = cursor.fetchall()
    conexao.close()
    if len(contatos) == 0:
        print("Nenhum contato encontrado.")
    else:
        print("### RESULTADO DA BUSCA ###")
        print(f"{'ID':<5} | {'Nome':<20} | {'Telefone':<15} | {'Email':<30}")
        print('-' * 80)
        for contato in contatos:
            print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")

def atualizar_contato():

    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''SELECT * FROM contatos'''
    cursor.execute(sql)
    contatos = cursor.fetchall()
    if len(contatos) == 0:
        print("Nenhum contato encontrado.")
    else:     
        id_contato = input("Digite o ID do contato que deseja atualizar: ")
        sql = '''SELECT * FROM contatos WHERE id = ?'''
        cursor.execute(sql, (id_contato,))
        contato = cursor.fetchone()
        if contato is None:
            print("Contato não encontrado.")
        else:
            novo_nome = input(f"Digite o novo nome (atual: {contato[1]}): ")
            novo_telefone = input(f"Digite o novo telefone (atual: {contato[2]}): ")
            novo_email = input(f"Digite o novo email (atual: {contato[3]}): ")
            sql = '''UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?'''
            cursor.execute(sql, (novo_nome, novo_telefone, novo_email, id_contato))
            conexao.commit()
            print("Contato atualizado com sucesso!")
        
def excluir_contato():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''SELECT * FROM contatos'''
    cursor.execute(sql)
    contatos = cursor.fetchall()
    if len(contatos) == 0:
        print("Nenhum contato encontrado.")
    else:
        id_contato = input("Digite o ID do contato que deseja excluir: ")
        sql = '''SELECT * FROM contatos WHERE id = ?'''
        cursor.execute(sql, (id_contato,))
        contato = cursor.fetchone()
        if contato is None:
            print("Contato não encontrado.")
        else:
            sql = '''DELETE FROM contatos WHERE id = ?'''
            cursor.execute(sql, (id_contato,))
            conexao.commit()
            print("Contato excluído com sucesso!")

def menu():
    while True:
        print("### CONTATOS ###")
        print("01. Adicionar contato")
        print("02. Listar contatos")
        print("03. Buscar contato pelo nome")
        print("04. Atualizar contato")
        print("05. Excluir contato")
        print("06. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "01":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            adicionar_contato(nome, telefone, email)
            print("Contato adicionado com sucesso!")
        elif opcao == "02":
            listar_contatos()
        elif opcao == "03":
            buscar_contato()        
        elif opcao == "04":
            atualizar_contato()
        elif opcao == "05":
            excluir_contato()
        elif opcao == "06":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")       

menu()
