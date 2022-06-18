from time import sleep
import viagens_módulo_1 as viagem

print('')
print('Olá! seja bem vindo(a)....')

loop = True
while loop == True:
    sleep(1/2)
    opcao = int(input('Selecione o tipo de atendimento desejado:\n[1] Dúvidas frequentes\n[2] Consultar as próximas viagens disponíveis\n[3] Informações adicionais\n[4] Sair\n'))
    sleep(1/2)
    if opcao == 1:
        print('a')  # Aqui entra uma estrutura condicional referente as opções Dúvidas frequentes [1]
    elif opcao == 2:
        if viagem.consulta() == False:
            print('Atendimento cancelado.')
            sleep(1)
            loop = False
    elif opcao == 3:
        print('b')  # Aqui entra uma estrutura condicional referente as opções Informações adicionais [3]
    elif opcao == 4:
        print('Muito obrigado por entrar em contato!')
        loop = False
    else:
        print('Opção indisponível, por favor, selecione uma das opções acima.')