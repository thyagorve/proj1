import subprocess
import os
import socket
import ssl
import random
import requests
import threading
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style
import time





os.system('clear')
coma1=[]
coma2=[]

#menu
def pintss():
    os.system('clear')
    print('｡☆✼★'+ ('━'*15)+'\033[34;1m SilvaSys Innovations 08/10/2022 \033[m'+('━'*15)+'★✼☆ ｡\n')
    print('\033[33mSistema desenvolvido por @Tiguinho  no entuto  de ajudar \nna procura de novos ips e host. Proibida a distribuição \nsem autorização\033[m\n')
    print('｡☆✼★'+ ('━'*10)+'\033[34;1m SELECIONE UMA OPÇAO A BAIXO \033[m'+('━'*10)+ '★✼☆ ｡\n')

    print('\033[31m[\033[m1\033[31m]\033[m ✼  Achar proxy(tim e vivo)')
    print('\033[31m[\033[m2\033[31m]\033[m ✼  Testar ip/host payloard(vivo e tim)')
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

        def check_proxy(ip):
            testar_conexao_sem_criptografia(ip, 443)

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

        qtd = (d - q) * 255

        # Use ThreadPool para limitar o número de threads ativas
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(check_proxy, coma1)

        print("Verificação de proxies concluída.")

 
    if res ==2:
        def check_ip(ip, contado, qtds, tested_ips):
            try:
                porta = 443
                if ip not in tested_ips:
                    testar_conexao_sem_criptografia(ip, porta)
                    tested_ips.add(ip)
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

            b = random.randint(1, 255)
            c = random.randint(1, 255)
            d = random.randint(1, 255)

            ggg = (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
            ips.append(ggg)

        qtds = len(ips)
        contado = 0
        tested_ips = set()  # Conjunto para rastrear IPs já testados

        threads = []

        for b in ips:
            contado += 1
            thread = threading.Thread(target=check_ip, args=(b, contado, qtds, tested_ips))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        print(f"Verificação de IPs concluída. Resultados salvos em '{output_filename}'.")




    agradecimento()  
def Testarhostproxydirect(): ###### Testar ip (vivo paylord)') ########

    init(autoreset=True)

    print_lock = threading.Lock()
    positive_proxies = []

    def check_proxy(proxy_host, cloudfront_host, status_to_save):
        try:
            # Estabelecer conexão com o proxy HTTP
            proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            proxy_socket.settimeout(0.5)  # Limite de tempo de 0.5 segundo
            proxy_socket.connect((proxy_host, 80))  # Tentar conectar ao proxy

            # Requisição a ser enviada ao CloudFront com o host específico
            cloudfront_request = f"GET / HTTP/1.1\r\nHost: {cloudfront_host}\r\nConnection: Upgrade\r\nUpgrade: Websocket\r\n\r\n"

            # Enviar a requisição GET com o valor de CLOUDFRONT
            proxy_socket.send(cloudfront_request.encode())

            # Receber a resposta do proxy
            response = proxy_socket.recv(4096)

            # Coletar o número do status HTTP
            status_code = response.split(b' ')[1]

            # Definir a cor e a mensagem de acordo com o status_code
            if status_code == b'200':
                color = Fore.YELLOW
                message = "Passou perto"
            elif status_code in [b'101', b'403']:
                color = Fore.GREEN
                message = "ONLINE"
                positive_proxies.append(proxy_host)
            else:
                color = Fore.RED
                message = "OFFLINE"

            # Bloquear o acesso ao print para garantir a exibição correta
            with print_lock:
                # Exibir a execução do proxy com a cor e mensagem adequadas
                print(f"{color}- {message} Status: {status_code.decode()} --> {proxy_host} - {cloudfront_host}")

            # Verificar se o status_code deve ser salvo
            if status_code.decode() in status_to_save:
                with open("status_saved.txt", "a") as status_file:
                    status_file.write(f"{proxy_host} - {cloudfront_host} - {status_code.decode()}\n")

            # Fechar a conexão com o proxy
            proxy_socket.close()

        except Exception as e:
            # Bloquear o acesso ao print para garantir a exibição correta
            with print_lock:
                # Exibir a execução do proxy com cor vermelha (erro)
                print(f"{Fore.RED}- OFFLINE {proxy_host}")

    def main():
        print(f"{Fore.GREEN}{Style.BRIGHT}Pressione Enter quando estiver no dados móveis...{Style.RESET_ALL}")
        input("")

        # Solicitar ao usuário se deseja usar o arquivo hosts.txt ou gerar IPs
        use_file = input("Deseja usar o arquivo hosts.txt (S/n)? ").strip().lower()

        if use_file == 's':
            # Ler hosts a partir do arquivo hosts.txt
            with open("hosts.txt", "r") as file:
                hosts = file.read().splitlines()
        else:
            perg = input('Digite dois grupos de 1 IP proxy:\n')
            q = int(input('Intervalo do 3° grupo - valor menor:\n'))
            d = int(input('Intervalo do 3° grupo - valor maior:\n'))

            if perg == "":
                perg = "255"
            else:
                perg = perg

            if q > d:
                q = int(input('Valor menor: '))
                d = int(input('Valor maior: '))

            ip_list = []
            for i in range(q, d + 1):
                for ii in range(1, 256):
                    r = (perg + '.' + str(i) + '.' + str(ii))
                    ip_list.append(r)

            hosts = ip_list

        # Solicitar até 5 hosts diferentes via entrada de dados
        cloudfront_hosts = []
        for i in range(5):
            host = input(f"Digite o {i + 1}º host para cloudfront (ou deixe em branco para usar o padrão): ")
            if host:
                cloudfront_hosts.append(host)

        # Se a lista de hosts estiver vazia, use o valor padrão
        if not cloudfront_hosts:
            cloudfront_hosts = ["d2ph342hr11u2x.cloudfront.net"]

        # Solicitar códigos de status para salvar
        status_to_save = input("Digite os códigos de status que deseja salvar (separados por espaço): ").split()

        # Exemplo de uso com ThreadPoolExecutor
        start_time = time.time()
        with ThreadPoolExecutor() as executor:
            futures = []
            
            for proxy_host in hosts:
                for cloudfront_host in cloudfront_hosts:
                    futures.append(executor.submit(check_proxy, proxy_host, cloudfront_host, status_to_save))

            # Aguardar a conclusão das tarefas
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print("Erro durante a execução do teste")

        execution_time = time.time() - start_time
        print("Tempo:", execution_time)

        # Exibir a lista de proxies positivos
        print("Proxies positivos:")
        for proxy in positive_proxies:
            print(proxy)

    if __name__ == '__main__':
        main()


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
        print(f"Indisponivel no momento.")



    agradecimento() 
    if sc ==5: ### Encontrar Dominios') ####
        print("ainda em")
        #EncontrarDominios()
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
