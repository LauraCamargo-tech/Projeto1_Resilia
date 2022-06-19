from time import sleep
import viagens_modulo_1 as viagens
from Informacoes_modulo_1 import informacao
from Duvidas_modulo_1 import duvidas
from Pacotes_adicionais_modulo_1 import adicionais

print('')
print('Olá! seja bem vindo(a)....')

loop = True
while loop == True:
    sleep(1/2)
    opcao = int(input('Selecione o tipo de atendimento desejado:\n[1] Dúvidas frequentes\n[2] Consultar as próximas viagens disponíveis\n[3] Informações adicionais\n[4] Pacotes adicionais\n[5] Sair\n'))
    sleep(1/2)
    if opcao == 1:
        duvidas()  # Laura
        if viagens.finalizar() == False: 
            print('Atendimento cancelado.')
            sleep(1)
            loop = False
    elif opcao == 2:
        if viagens.consulta() == False: # Lucas
            print('Atendimento cancelado.')
            sleep(1)
            loop = False
    elif opcao == 3:
        informacao()  # Amanda
        if viagens.finalizar() == False: 
            print('Atendimento cancelado.')
            sleep(1)
            loop = False
    elif opcao == 4:
        adicionais()  # Amanda
        if viagens.finalizar() == False: 
            print('Atendimento cancelado.')
            sleep(1)
            loop = False
    elif opcao == 5:
        print('Muito obrigado por entrar em contato!')
        loop = False
    else:
        print('Opção indisponível, por favor, selecione uma das opções acima.')