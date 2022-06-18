from time import sleep

# def linha (tam = 70 ): #deseja uma linha na tela, com valor padrão de 42
#     return '-'*tam     # desenha essa - vezes a quantidade informada ou usa o padrão definido

def finalizar():
    resetar = int(input('Selecione:\n[1] Resetar o atendimento\n[2] Finalizar o atendimento\n'))
    if resetar == 1:
        return True
    elif resetar == 2:
        return False
    else:
        print('Insira uma opção válida!')
        sleep(1/2)
        finalizar()

def consulta():

    nacionalidade = int(input('Que tipo de viagem você deseja realizar?\n[1] Nacional\n[2] Internacional \n[3] Sair\n'))
    if nacionalidade == 3:
        return False
    sleep(1/2)
    tempo = int(input('Quando você deseja realizar a viagem?\n[1] Dentro de 6 meses\n[2] Dentro de 1 ano\n[3] Mais de 1 ano \n[4] Sair\n'))
    if tempo == 4:
        return False
    sleep(1/2)

    if nacionalidade == 1:

        if tempo == 1:
            nacional_6 = int(input('Próximas viagens nacionais disponíveis dentro de 6 meses: \n\n[1] Porto de Galinhas - Pernambuco ---------- R$999\n[2] Foz do Iguaçu - Paraná ------------------ R$849\n'))

            if nacional_6 == 1:
                print('o pacote Porto de Galinhas - Pernambuco vem incluso Hospedagem, Café da manhã e a passagem aérea, o preço é individual e referente a 3 diárias, podendo ser aumentada para 5 ou 7.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif nacional_6 == 2:
                print('o pacote Foz do Iguaçu - Paraná vem incluso Hospedagem, Café da manhã e a passagem aérea, o preço é individual e referente a 3 diárias, podendo ser aumentada para 5 ou 7.\n')
                fim = finalizar()
                if fim == False:
                    return False
            else:
                print('Por favor, selecione um pacote válido!')
    
        elif tempo == 2:
            nacional_12 = int(input('Próximas viagens nacionais disponíveis dentro de 1 ano: \n\n[1] Chapada dos Guimarães - Mato Grosso --- R$659\n[2] Beto Carrero World - Santa Catarina --- R$769\n[3] Recife - Pernambuco ------------------- R$399\n'))

            if nacional_12 == 1:
                print('O pacote Chapada dos guimarães - Mato Grosso vem incluso hospedagem, café da manhã, Aluguel de carro e a Passagem aérea, o preço é individual e referente a 3 diárias, podendo ser aumentada para 5 ou 7.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif nacional_12 == 2:
                print('O pacote Beto Carrero World - Santa Catarina vem incluso hospedagem, café da manhã, ingresso para 1 dia de parque e a Passagem aérea, o preço é individual e referente a 3 diárias, podendo ser aumentada para 5 ou 7.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif nacional_12 == 3:
                print('O pacote Recife - Pernambuco vem incluso hospedagem, café da manhã e a Passagem aérea, o preço é individual e referente a 3 diárias, podendo ser aumentada para 5 ou 7.\n')
                fim = finalizar()
                if fim == False:
                    return False
            else:
                print('Por favor, selecione um pacote válido!')
        
        elif tempo == 3:

            nacional_12mais = int(input('Próximas viagens nacionais disponíveis para mais de 1 ano: \n\n[1] Jericoacoara + Fortaleza - Ceará ------- R$799\n'))

            if nacional_12mais == 1:
                print('O pacote Jericoacoara + Fortaleza - Ceará vem incluso hospedagem, café da manhã,  e a Passagem aérea, o preço é individual e referente a 5 diárias, podendo ser aumentada para 7.\n')
                fim = finalizar()
                if fim == False:
                    return False

        else:
            print('Por favor, selecione uma data válida!')
            consulta()


    elif nacionalidade == 2:

        if tempo == 1:
            internacional_6 = int(input('Próximas viagens internacionais disponíveis dentro de 6 meses:\n\n[1] Madrid + Barcelona - Espanha ------ R$5939\n[2] Toronto - Canadá ------------------ R$5539 '))

            if internacional_6 == 1:
                print('O pacote Madri + Barcelona vem incluso hospedagem e a passagem aérea, o preço é individual e referente a 8 diárias.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif internacional_6 == 2:
                print('O pacote Toronto - Canadá vem incluso hospedagem e a passagem aérea, o preço é individual e referente a 5 diárias, podendo ser aumentada para 7 ou 9.\n')
                fim = finalizar()
                if fim == False:
                    return False
            else:
                print('Por favor, selecione um pacote válido!')

        elif tempo == 2:

            internacional_12 = int(input('Próximas viagens internacionais disponíveis dentro de 1 ano:\n\n[1] Japão - Tóquio ------------------ R$3849 \n[2] Orlando - Estados Unidos -------- R$2889 \n[3] Atenas + Santorini - Grécia ----- R$3599\n'))

            if internacional_12 == 1:
                print('O pacote Japão - Tóquio vem incluso hospedagem e passagem aérea, o preço é individual e referente a 7 diárias, podendo ser aumentada para 10.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif internacional_12 == 2:
                print('O pacote Orlando - Estados Unidos vem incluso hospedagem e passagem aérea, o preço é individual e referente a 7 diárias, podendo ser aumentada para 14.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif internacional_12 == 3:
                print('essa é a opção 3 inter 1a\n')
                fim = finalizar()
                if fim == False:
                    return False
            else:
                print('Por favor, selecione um pacote válido!')
            
        elif tempo == 3:

            internacional_12mais = int(input('Próximas viagens internacionais disponíveis para mais de 1 ano: \n\n[1] Las Vegas - Estados Unidos -------- R$2749\n'))

            if internacional_12mais == 1:
                print('O pacote Las Vegas - Estados Unidos vem incluso hospedagem e passagem aérea, o preço é individual e referente a 5 diárias, podendo ser aumentada para 7.\n')
                fim = finalizar()
                if fim == False:
                    return False
            else:
                print('Por favor, selecione um pacote válido!')
                    
        else:
            print('Por favor, selecione uma data válida!')
            consulta()

    else:
        print('Opção de viagem não disponível, por favor, escolha outra!')
        sleep(1/2)
        consulta()

def duvidas():
        print('\n[1] Hospedagem? \n[2] Viagem? \n[3] Sair\n')
        opcao = int(input('Digite qual tipo da sua duvida :  '))
        if opcao == 1:
            print('\n[1] Qual meu hotel e quarto ?\n[2] Qual valor da diária?\n[3]Como cancelar minha hospedagem ?\n[4]Voltar ao Menu inicial\n')
            opcao = int(input('Digite a opção que representa sua dúvida :  '))
            if opcao == 1 :
                site = 'https://suaviagemresilia.com/reserva/'
                print(f'\nFaça seu login em {site}, em seu perfil encontrara o hotel e quarto escolhidos\n' )
            elif opcao == 2:
                site = 'https://suaviagemresilia.com/reserva/diária'
                print(f'\nFaça seu login em {site}, em seu perfil encontrara o valor da diária\n' )
            elif opcao == 3:
                site = 'https://suaviagemresilia.com/reserva/cancelamento'
                print(f'\nFaça seu login em {site}, em seu perfil encontrara a opçao de cancelamento\n' )
            else:
                return False
            sleep(1/2)
        elif opcao == 2:
            print('\n[1] Qual horário do meu voo ?\n[2] Como reservar uma passagem aerea?\n[3]Posso transportar animais ?\n[4]Voltar ao Menu inicial\n')
            opcao = int(input('Digite a opção que representa sua dúvida :  '))
            if opcao == 1 :
                site = 'https://suaviagemresilia.com/horário/'
                print(f'\nFaça seu login em {site}, em seu perfil encontrara o horário de seu voo\n' )
            elif opcao == 2:
                site = 'https://suaviagemresilia.com/passagem/'
                print(f'\nAtravés de nosso site: {site}, encontrara varias opções e seus respectivos valores\n' )
            elif opcao == 3:
                site = 'https://suaviagemresilia.com/reserva/cancelamento'
                print(f'O transporte de animais domésticos, tais como cachorros e gatos, deve autorizá-lo a companhia aérea. Consulte as condições da companhia no ato da reserva\n' )
            else:
                return False

