import subprocess
import os
import socket
import ssl
import random
import requests
import threading
import concurrent.futures




os.system('clear')
coma1=[]
coma2=[]

#menu
def pintss():
    os.system('clear')
    print('｡☆✼★'+ ('━'*15)+'\033[34;1m TIAGO LIMA SILVA \033[m'+('━'*15)+'★✼☆ ｡\n')
    print('\033[33mSistema desenvolvido por tiago lima  no entuto  de ajudar \nna procura de novos ips e host. Proibida a distribuição \nsem autorização\033[m\n')
    print('｡☆✼★'+ ('━'*10)+'\033[34;1m SELECIONE UMA OPÇAO A BAIXO \033[m'+('━'*10)+ '★✼☆ ｡\n')

    print('\033[31m[\033[m1\033[31m]\033[m ✼  Achar proxy(todas op)')
    print('\033[31m[\033[m2\033[31m]\033[m ✼  Testar ip (vivo)')
    print('\033[31m[\033[m3\033[31m]\033[m ✼  Testar host ssl(vivo,tim,claro)')
    print('\033[31m[\033[m4\033[31m]\033[m ✼  Encontra Cloudflare(off)')
    print('\033[31m[\033[m5\033[31m]\033[m ✼  Encontrar Dominios')
    print('\033[31m[\033[m6\033[31m]\033[m ✼  Encontrar CDN\n')
    print('━'*55)
    menu() 
def achaproxy():  ###### Achar proxy(vivo)')#######
    #print('━'*30)
    print("\n")  
    print('\033[31m[\033[m1\033[31m]\033[m ✼  Aleatorio')
    print('\033[31m[\033[m2\033[31m]\033[m ✼  Random\n')
    res = int(input("Selecione um formato de proxy: "))  
 
    if res == 1:


        def testar_conexao_sem_criptografia(host, porta):
            try:     
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((host, porta))
                print(f"\033[32m- ✅ - {host} ONLINE!!\033[m")
                with open(output_filename, "a") as arquivo:
                    arquivo.write(host + '\n')
                sock.close()
            except socket.error:
                print(f"\033[31m- 🔴 - {host} OFF !!\033[m")
                pass
        def check_proxy(ip, contado, qtd):
            try:            
               testar_conexao_sem_criptografia(ip, 443)
            except:
               pass

        perg = input('Digite dois grupos de 1 IP proxy:\n')
        q = int(input('Intervalo 3° grupo valor menor:\n'))
        d = int(input('Intervalo 3° grupo valor maior:\n'))
        output_filename = input('Digite o nome do arquivo de saída (ex: proxyativo2.txt): ')

        if perg == "":
            perg = "255"
        else:
            perg = perg

        if q > d:
            q = int(input('Valor menor:\n'))
            d = int(input('Valor maior:\n'))

        coma1 = []

        for i in range(q, d):
            for ii in range(1, 256):
                r = (perg + '.' + str(i) + '.' + str(ii))
                coma1.append(r)

        threads = []
        contado = 0
        qtd = (d - q) * 255

        for b in coma1:
            contado += 1
            thread = threading.Thread(target=check_proxy, args=(b, contado, qtd))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        print("Verificação de proxies concluída.")

 
    if res ==2:


        def check_ip(ip, contado, qtds):
            try:
                porta = 443
                testar_conexao_sem_criptografia(ip, porta)

                                     
            except:
               pass


        def testar_conexao_sem_criptografia(host, porta):
            try:

                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((host, porta))
                print(f"\033[32m- ✅ - {host} ONLINE!!\033[m")
                with open(output_filename, "a") as arquivo:
                    arquivo.write(host + '\n')
                sock.close()
            except:
                print(f"\033[31m- 🔴 - {host} OFF !!\033[m")
                
        qtd = int(input('Quantos IPs você deseja?: '))
        q = input('Valor inicial: ')
        output_filename = input('Digite o nome do arquivo de saída (ex: proxyativo2.txt): ')

        ips = []

        for i in range(qtd):
            if q == "":
                a = random.randint(1, 255)
            else:
                a = q

            if a == 127:
                a = random.randint(1, 255)

            if a == 127:
                a = random.randint(1, 255)

            if a == 127:
                a = random.randint(1, 255)

            if a == 127:
                a = random.randint(1, 255)

            b = random.randint(1, 255)
            c = random.randint(1, 255)
            d = random.randint(1, 255)

            ggg = (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
            ips.append(ggg)

        qtds = len(ips)
        contado = 0

        threads = []

        for b in ips:
            contado += 1
            thread = threading.Thread(target=check_ip, args=(b, contado, qtds))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        print(f"Verificação de IPs concluída. Resultados salvos em '{output_filename}'.")



    agradecimento()  
def Testarhostproxydirect(): ###### Testar ip (vivo)') ########
  try:
    with open("proxy.txt", "r") as tf:
        coma2 = tf.read().split('\n')

    with open("proxy.txt", "r") as file:
        Counter = 0
        Content = file.read() 
        CoList = Content.split("\n") 
        for i in CoList: 
            if i: 
                Counter += 1

    contado=0
    with open(os.devnull, "wb" ) as limbo:
              for b in coma2:
                  contado=contado+1
                  try:
                            result=subprocess.Popen(["ping", "-c", "1", "-n","-w","5", b],
                                  stdout=limbo, stderr=limbo).wait( timeout=0.1)
                            if result:
                                  print(f"\033[31m - {contado} de {Counter} - " + b )
                            else:
                                  print(f"\033[32m- {contado}  de {Counter} -" + b )
                                  with open("proxytestados.txt", "a") as arquivo:
                                          arquivo.write('\n' +b)                                             
                  except:
                          print(f"\033[31m- {contado} de {Counter} - " + b )
    agradecimento()
  except FileNotFoundError:
    print('\033[31mnão encontrado o arquivo proxy.txt\033[m')
    agradecimento()
def Testarhostssl(): #### Testar ssl(vivo,tim,claro)') ####


    def check_host(b, contado):
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

            with socket.create_connection((b, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=b) as sslsock:
                    der_cert = sslsock.getpeercert(True)
                    pem_cert = ssl.DER_cert_to_PEM_cert(der_cert)
            print(f"\033[32m--> " + b)

            with open(output_filename, "a") as arquivo:
                arquivo.write(b + '\n')  # Adicione uma nova linha no final
        except:
            print(f"\033[31m --> " + b)

    def main():
        try:
            

            with open(input_filename, "r") as tf:
                coma = tf.read().split('\n')

            file = open(input_filename, "r")
            Counter = 0
            Content = file.read()
            CoList = Content.split("\n")
            for i in CoList:
                if i:
                    Counter += 1
            contado = 0

            

            with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
                futures = []
                for b in coma:
                    contado += 1
                    futures.append(executor.submit(check_host, b, contado))

                for future in concurrent.futures.as_completed(futures):
                    pass  # Aguarda a conclusão das threads

            print('\n\n\033[32mVerificação concluída!\n\n')
            agradecimento()
        except FileNotFoundError:
            print(f'\033[31mArquivo {input_filename} não encontrado.\033[m')
            pass



    if __name__ == "__main__":
        input_filename = input('Digite o nome do arquivo de entrada (exemplo: hostteste.txt): ')
        output_filename = input('Digite o nome do arquivo de saída (exemplo: host.txt): ')
        num_threads = int(input('Digite a quantidade de threads desejada: '))
        main()


    
   # agradecimento()          
def Encontracdn(): #### Encontrar CDN\n') ####
    opcao = input("Seu arquivo está em um arquivo de texto? (Digite 1 para sim, 2 para não): ")

    if opcao == "1":
        nome_arquivo = input("Digite o nome do arquivo de texto (exemplo: arquivo.txt): ")
        with open(nome_arquivo, "r") as tf:
            cloudd = tf.read().split('\n')
    else:
        host = input('Digite o nome do host: ')
        cloudd = [host]  # Crie uma lista com o nome do host

    for iii in cloudd:
        ip = socket.gethostbyname(iii)
        print(f'O IP do Host {iii} é {ip}')
        
        url = f"https://rdap.arin.net/registry/ip/{ip}"

        response = requests.get(url)

        if response.status_code == 200:
            rr = response.json()
            try:
                nomedabagaca = rr['name']
                print(f'{nomedabagaca} - {iii}')
                with open(f"suscesso-{nomedabagaca}.txt", "a") as arquivo:
                    arquivo.write('\n' + iii)
            except:
                print('Nome de domínio não encontrado')
        else:
            print('Erro ao acessar o serviço de consulta de IP.')

    agradecimento()    
def menu():
    sc = int(input('Qual sua escolha? '))
    if sc ==1: ###### Achar proxy(vivo)')#######
        achaproxy()
    if sc ==2: ###### Testar ip (vivo)')
        Testarhostproxydirect()
    if sc ==3: #### Testar ssl(vivo,tim,claro)') 
        Testarhostssl()
    if sc ==4: ### Encontra Cloudflare') ####
        EncontraCloudflare()
    if sc ==5: ### Encontrar Dominios') ####
        EncontrarDominios()
    if sc ==6: #### Encontrar CDN\n') ####
        Encontracdn()
def buscahostedominio():
  vao=int(input('informe quantas deseja: '))
  for y in range ():
    response = requests.get("https://random-word-form.herokuapp.com/random/noun")  
    rrrs= response.json()
    #print(rrrs)
    for e in rrrs:   
        try:        
                                  
                response = requests.get("https://api.domainsdb.info/v1/domains/search?domain=" +e + "&zone=")
             
                rrr= response.json()
                #    print (response.status_code)
                    
                if (response.status_code == 200):
                        for ii in rrr['domains']:
                            ip = socket.gethostbyname(ii['domain'])
        
              
                            url = ("https://rdap.arin.net/registry/ip/"+ip)
        
                            response = requests.request("GET", url)
        
                            rr= response.json()
              
            
                            if (rr['name'])=="CLOUDFLARENET":
                               
                                 with open("ativo-clodflare.txt", "a") as arquivo:
                                    arquivo.write(ii['domain']+'\n')
                            if (rr['name'])=="AMAZO-CF":

                                   with open("ativo-front.txt", "a") as arquivo:
                                        arquivo.write( ii['domain']+'\n')
                            if (rr['name'])=="GOOGLE":
                               # print ("GOOGLE", G, end='\r')
                                  with open("ativo-google.txt", "a") as arquivo:
                                    arquivo.write( ii['domain']+'\n')    
                             
                            if (rr['name'])=="GOOGLE-CLOUD":
                                #print ("GOOGLE", G, end='\r')
                                with open("ativo-google-cloud.txt", "a") as arquivo:
                                    arquivo.write( ii['domain']+'\n')         
                            if (rr['name'])=="SKYCA-3":
                                #print ("GOOGLE", G, end='\r')
                                with open("ativo-Fastly-cloud.txt", "a") as arquivo:
                                    arquivo.write( ii['domain']+'\n' )                                                                                        
        except:
            pass
def agradecimento():
    #os.system('clear')
    print('\n\n\033[32mObrigado por usar nosso sistema!!\033[m\n\n')  
    print('｡☆✼★'+ ('━'*10)+'\033[34;1m DESEJA CONTINUAR NO SCRIPT? \033[m'+('━'*10)+ '★✼☆ ｡\n')

    print('\033[31m[\033[m1\033[31m]\033[m ✼  SIM')
    print('\033[31m[\033[m2\033[31m]\033[m ✼  NÃO\n')
    ssc = input("Selecione um numero? ")
    if ssc == "1" or ssc == "sim" or ssc == "Sim" or ssc == "SIM":
      pintss()
   
    elif ssc == "2" or ssc == "nao" or ssc == "Nao" or ssc == "não" or ssc == "Não" or ssc == "NAO" or ssc == "NÃO":
      os.system('clear') 
      print("\n\n\033[32mobrigado por usar nosso sistema. Jessus crito lhe abençoe.!!\033[m\n\n")
    else:
       print("\nOpção inválida. Por favor, selecione 1 para SIM ou 2 para NÃO.")
      
pintss()
