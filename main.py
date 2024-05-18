# Importações
import os
import time

# Funções
def saudar(version):
    print(f'''
        Mode v{version}
        Seja bem vindo
    ''')

def listar(a):
    if "/" in a or "\\" in a:
        valor = os.listdir(a)
        return valor
    else:
        return False
        
def stay_or_no_op(serviço):
    while True:
        x = str(input(f'''
            Deseja {serviço} mais arquivos? (s/n) '''))
        if x == "s":
            print("Ok")
            time.sleep(1)
            return True
            break
            
        elif x == "n":
            print("Ok")
            return False
            break
        else:
            print(erro_resposta)

            

# Variáveis Padrão
version = ('1.0') #Versão programa

ops = ['1', '2', '3'] #Opções primárias do programa
ops_nomes = ['Listar', 'Renomear']

erro_resposta = "Resposta Inválida, vamos tentar novamente?"


# Saudação
saudar(version)

# Loop Principal
while True:
    op = str(input('''
        Certo qual operação você deseja fazer?
        (1) Listar Arquivos
        (2) Renomear Arquivos
        (3) Sair do programa   
    '''))

    if op in ops:
        match op:
            case '1':
                # Pegar Diretório
                while True:
                    dir = input('''
                        Digite ou cole o Diretório:
                    ''')
                    listagem = listar(dir)
                    
                    if listagem == False:
                        print("Seu diretório é inválido! Vamos tentar novamente")
                        time.sleep(2)
                    else:
                        print('''
                              Prontinho sua lista de arquivos está logo abaixo!
                            ''')
                        print(listagem)
                        time.sleep(3)
                        stay_or_no_op(ops_nomes[0])
                        if stay_or_no_op == True:
                            print("Certo")
                        elif stay_or_no_op == False:
                            print("Certo agora você")


                            
            case '2':
                # Pegar Diretório
                dir = input('''
                    Digite ou cole o Diretório:
                ''')
                renomear = renomear(dir)
            
            case '3':
                print("Volte Sempre")
                break

    else:
        print(erro_resposta)
        



    
