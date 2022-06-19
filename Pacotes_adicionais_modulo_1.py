import os

def adicionais ():    
   pacoteAdd = int(input('Qual Serviço deseja adicionar?\n[1]-Aluguel de Carros\n[2]-Seguro Viagem\n[3]-Passeios não inclusos no pacote\n[4]-Sair\n'))
   #OPIÇÃO 1
   if (pacoteAdd == 1): 
      os.system("cls")
      opcaocarro =  int(input('Acesse o site: https://www.localiza.com/?\nEsta informacao foi util ?\n[1]-Sim\n[2]-Não\n')) 
      if opcaocarro == 2:
         os.system("cls")
         exit( ) 
         # tem que ver o que vai chamar
      #tratativa de erros de opcaocarro
      elif (opcaocarro != 1 or 2):
            print('Insira uma opção válida!')
         # addPacote() # tem que ver o que vai chamar
            
   #OPIÇÃO 2
   elif (pacoteAdd == 2):
      os.system("cls")
      opcaoSeguro = int(input('Acesse o site: https://assistentedeviagem.com.br/\nEsta informacao foi util ?\n[1]-Sim\n[2]-Não\n')) 
      if opcaoSeguro == 2:
         os.system("cls")
         exit( ) # tem que ver o que vai chamar
      #tratativa de erros de opcaoSeguro
      elif (opcaoSeguro != 1 or 2):
            print('Insira uma opção válida!')
            exit() # tem que ver o que vai chamar
   #OPIÇÃO 3
   elif (pacoteAdd == 3):
      os.system("cls")
      #direcionar para o site ficticio
      opcaoPacotesA = int(input('Acesse o site: https://assistentedeviagem.com.br/\nEsta informacao foi util ?\n[1]-Sim\n[2]-Não\n')) 
      if opcaoPacotesA == 2:
         os.system("cls")
         exit( ) # tem que ver o que vai chamar
      #tratativa de erros de opcaoSeguro
      elif (opcaoPacotesA != 1 or 2):
            print('Insira uma opção válida!')
            exit() # tem que ver o que vai chamar
   #OPIÇÃO 4
   elif (pacoteAdd == 4):
         
            exit() # tem que ver o que vai chamar
   #tratativa de erros de pacoteAdd
   elif (pacoteAdd != 1 or 2 or 3 or 4):
      print('Insira uma opção válida!')
      exit() # tem que ver o que vai chamar