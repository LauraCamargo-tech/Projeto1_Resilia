# desenvolver um código que vai listar X opções de
# atendimento (Ex: 1 - Dúvidas, 2 - Consultas, 3 - Informações, 4 - Sair) e o usuário
# será guiado por mensagens avançando dentro desse atendimento simulado até
# que chegue ao final obtendo a resposta desejada.
from time import sleep
import modulos

opcao = 0 #inciando o valor da opção

while opcao != 4 :

    # modulos.menu(opcao)
    print (f'       [1] Dúvidas\n       [2] Consultas\n       [3] Informações\n       [4] Sair')
    opcao = int(input('Olá! Para que possa te ajudar. Digite o número da opção desejada :  '))

    if opcao == 1:
        print(f'       [1] Dúvidas sobre a hospedagem ?\n       [2] Dúvidas sobre a viagem?')
        opcao = int(input('Digite a opção que representa sua dúvida :  '))
        if opcao == 1:
            print(f'       [1] Qual meu hotel e quarto ?\n       [2] Qual valor da diária?\n       [3]Como cancelar minha hospedagem ?\n       [4]Voltar ao Menu inicial')
            opcao = int(input('Digite a opção que representa sua dúvida :  '))
        elif opcao == 1 :
            site = 'https://suaviagemresilia.com/reserva/'
            print(f' Faça seu login em {site}, em seu perfil encontrara o hotel e quarto escolhidos' )
        elif opcao == 2:
            site = 'https://suaviagemresilia.com/reserva/diária'
            print(f' Faça seu login em {site}, em seu perfil encontrara o valor da diária' )
        elif opcao == 3:
            site = 'https://suaviagemresilia.com/reserva/cancelamento'
            print(f' Faça seu login em {site}, em seu perfil encontrara a opçao de cancelamento' )
        else: 
            print ('De volta ao menu inicial')
    elif opcao == 2:
        print ('        [1] Internacional\n       [2] Nacional')
        opcao = int(input('Qual tipo de viajem você deseja realiza ? '))
    elif opcao == 3 :
        print ('       1] Horários de voos reagendados\n       [2] Voos cancelados')
        opcao = int(input('Qual informação deseja ter ?  '))
    elif opcao == 4 :
        print ('Espero ter ajudado! Volte sempre :) ')
        break
    else:
        print('Opção invalida. Digite uma opção valida para obter a resposta desejada') 
    print(modulos.linha()) 
    sleep(3)
    
# print ('Espero ter ajudado! Volte sempre :) ')
