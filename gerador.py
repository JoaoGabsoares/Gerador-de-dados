import random

def dados():  
     
    print('Seja bem vindo, escolha as opções desejadas, obs: caso seja mais de uma , separe por virgula. exemplo, 1,2,3,4. Caso queira parar, digite "parar". \n')
   
   
    opcoes_escolha = input('Escolha as opções desejadas abaixo \n'
                           '[1]-nomes \n'
                           '[2]-Telefones \n'
                           '[3]-Emails \n'
                           '[4]-cidades \n'
                           '[5]-estados \n ' 'Escolha o Número desejado: ')
    
   
    nomes = ['Carlos Augusto','Cristiane Monteiro', 'Enderson Carvalho', 'Marcos da Silva', 'André Pereira']
    estados = ['Rio de janeiro', 'São Paulo', 'Minas Gerais', 'Bahia', 'Rio Grande do Sul']
    #############################################################
    
    #gerar numeros aleatorios
    numero_telefone = [5521997849041, 5511946787898, 5523987975897, 5512994788974, 5522994788950]
    
    #############################################################
    
    emails = ['adasesa@gmail.com', 'asdasojo@hotmail.com', 'Asdasdxcb@gmail.com', 'skpz@gmail.com', 'sdap@hotmail.com']
    cidades = ['Rio de janeiro', 'São Paulo', 'Salvador', 'Belo-Horizonte', 'Porto Alegre']
    
    for escolha in opcoes_escolha:
        if escolha == '1':
            print(random.choice(nomes))
        elif escolha == '2':
            print(random.choice(numero_telefone))
        elif escolha == '3':
            print(random.choice(emails))
        elif escolha == '4':
            print(random.choice(cidades))
        elif escolha == '5':
            print(random.choice(estados))
        elif escolha == 'parar':
            exit()
        
            
    

dados()