# Importações
import os

# Funções
def saudar(a):
    print(f'''
        Mode v{a}
        Seja bem vindo
    ''')

def listar(a):
    return os.listdir(a)
# Variáveis Padrão
version = ('1.0')

ops = [1, 2, 3]

# Programa
programa = True
while True:
    # Saudação
    saudar(version)

    while True:
        op = input('''
            Certo qual operação você deseja fazer?
            (1) Listar Arquivos
            (2) Renomear Arquivos
            (3) Sair do programa   
        ''')
        if op in ops:
            match op:
                case 1:
                    # Pegar Diretório
                    dir = input('''
                        Digite ou cole o Diretório:
                    ''')

                    listagem = listar(dir)

                    print(listagem)
                
                case 2:
                    print("Ainda não pronto")
                
                case 3:
                    print("Ainda não pronto")
        else:
            
        



    
