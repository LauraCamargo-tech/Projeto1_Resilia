def linha (tam = 70 ): #deseja uma linha na tela, com valor padrão de 42
    return '-'*tam     # desenha essa - vezes a quantidade informada ou usa o padrão definido

def menu (opcao):
    print (f'       [1] Dúvidas\n       [2] Consultas\n       [3] Informações\n       [4] Sair')
    opcao = int(input('Olá! Para que possa te ajudar. Digite o número da opção desejada :  '))
    return opcao