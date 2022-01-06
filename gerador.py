import random

def dados():  
     
    print('Seja bem vindo, escolha as opções desejadas, obs: caso seja mais de uma , separe por virgula. exemplo, 1,2,3,4. Caso queira parar, digite parar.')
    opcoes_escolha = input('Escolha as opções desejadas abaixo: \n'
                           '[1]-nomes \n'
                           '[2]-Telefones \n'
                           '[3]-Emails \n '
                           '[4]-cidades \n'
                           '[5]-estados \n ' 'Escolha o Número desejado: ')
    
   
    nomes = ['Carlos Augusto','Cristiane Monteiro', 'Enderson Carvalho', 'Marcos da Silva', 'André Pereira']
    estados = ['Rio de janeiro', 'São Paulo', 'Minas Gerais', 'Bahia', 'Rio Grande do Sul']
    #############################################################
    #gerar numeros aleatorios
    numero_telefone = list(range(0,9))
    random.shuffle(numero_telefone)
    #print(numero_telefone)
    #############################################################
    emails = ['adasesa@gmail.com', 'asdasojo@hotmail.com', 'Asdasdxcb@gmail.com', 'skpz@gmail.com', 'sdap@hotmail.com']
    cidades = ['Rio de janeiro', 'São Paulo', 'Salvador', 'Belo-Horizonte', 'Curitiba']
    
    if (opcoes_escolha == '1'):
        print(random.choice(nomes))
        
    elif (opcoes_escolha == '2'):
        print( numero_telefone)
        
    elif (opcoes_escolha == '3'):
        print(random.choice(emails))
    
    elif (opcoes_escolha == '4'):
        print(random.choice(cidades))
    
    elif (opcoes_escolha == '5'):
        print(random.choice(estados))
    
    elif (opcoes_escolha == 'parar'):
        exit()
        
        
    
    

dados()