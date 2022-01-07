import random
import logging

def dados():  
     
     
     while True:
         
        logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',format='%(levelname)s - %(message)s - %(asctime)s')
         
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
            
            
        try:
                    
            for escolha in opcoes_escolha:
                if (escolha == '1'):
                        nome = random.choice(nomes)
                        print(random.choice(nomes))
                        logging.info(f'O nome gerador foi {nome}')
                elif (escolha == '2'):
                        number = random.choice(numero_telefone)
                        print(random.choice(numero_telefone))
                        logging.info(f'O número gerado foi {number}')
                elif (escolha == '3'):
                        email = random.choice(emails)
                        print(random.choice(emails))
                        logging.info(f'O email gerado foi {email}')
                elif( escolha == '4'):
                        city = random.choice(cidades)
                        print(random.choice(cidades))
                        logging.info(f'A cidade gerada foi {city}')
                elif (escolha == '5'):
                        state = random.choice(estados)
                        print(random.choice(estados))
                        logging.info(f'O estado gerado foi {state}')
                else:
                    pass
            
            if (opcoes_escolha == 'parar'):
                logging.info('O programa foi finalizado')
                exit()
           
        except ValueError as erro:
            print('Favor Digitar Corretamente')
            logging.warning(erro)
    

dados()