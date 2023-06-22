from colorama import Fore, Style
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from colorama import init, Fore
import ssl
import random
import threading


def clear_screen():
    print("\033c", end="")

def show_menu():
    clear_screen()
    print(f"{Fore.BLUE}=== BEM-VINDO AO TLSNET ==={Style.RESET_ALL}\n")
    print("Selecione uma opção:")
    print("1. ENCONTRA IP DA HOST")
    print("2. TESTE DE CONEXÃO Proxy/Direct")
    print("3. TESTE DE CONEXÃO TLS/SSL Proxy")
    print("4. GERA IP PARA TESTE NO SIST")
    print("0. Sair")

def get_user_choice():
    choice = input("Digite o número da opção desejada: ")
    return choice

def main():
    while True:
        show_menu()
        choice = get_user_choice()
        if choice == '0':
            print("Saindo do programa...")
            break
############################################################################################################################         
        elif choice == '1':
            op =int(input("digite 1 para informa o dominio ou 2 para puxar txt: "))
            
            if op == 1:

                clear_screen()
                def get_all_ips(domain):
                    try:
                        ips = socket.gethostbyname_ex(domain)
                        return ips[2]
                    except socket.gaierror:
                        return []

                domain = input("Digite o domínio: ")
                ips = get_all_ips(domain)

                if ips:
                        print(f"Endereços IP do domínio '{domain}':")
                        for ip in ips:
                            print(ip)   
                else:
                    print(f"Não foi possível encontrar endereços IP para o domínio '{domain}'.")
            elif op ==2:
                clear_screen()    

                def get_all_ips(domain):
                    try:
                        ips = socket.gethostbyname_ex(domain)
                        return ips[2]
                    except socket.gaierror:
                        return []
                
                # Ler domínios de um arquivo de texto
                def read_domains_from_file(filename):
                    with open(filename, "r") as file:
                        domains = file.read().splitlines()
                    return domains
                
                # Nome do arquivo de texto contendo os domínios
                filename = input("Digite o nome do arquivo de texto: ")
                output_filename = input("Digite o nome do arquivo de saída: ")
                
                domains = read_domains_from_file(filename)
                
                if domains:
                    total_hosts = len(domains)
                    unique_ips = set()  # Conjunto para armazenar IPs únicos
                    hosts_tested = 0
                    hosts_remaining = total_hosts
                    collected_ips = []  # Lista para armazenar todos os IPs coletados
                
                    for domain in domains:
                        domain = domain.strip()  # Remover espaços em branco antes e depois do domínio
                
                        if domain:  # Verificar se o domínio não está vazio
                            try:
                                ips = get_all_ips(domain)
                                if ips:
                                    for ip in ips:
                                        unique_ips.add(ip)  # Adicionar IP ao conjunto
                                        collected_ips.append(ip)  # Adicionar IP à lista de IPs coletados
                                        print(ip)  # Exibir o IP coletado
                                else:
                                    print(f"Não foi possível encontrar endereços IP para o domínio '{domain}'.")
                            except Exception as e:
                                print(f"Erro ao processar o domínio '{domain}': {e}")
                
                        hosts_tested += 1
                        hosts_remaining -= 1
                        print(f"Hosts testados: {hosts_tested}/{total_hosts}")
                        print(f"Hosts restantes: {hosts_remaining}")
                
                    # Gravar os IPs coletados no arquivo de saída
                    with open(output_filename, "w") as output_file:
                        for ip in collected_ips:
                            output_file.write(ip + "\n")
                
                    print("Coleta de IPs concluída!")
                else:
                    print("Arquivo vazio ou não encontrado.")
                
                               
                                
                
                
                

############################################################################################################################        
        elif choice == '2':
            clear_screen()
            init(autoreset=True)

            print_lock = threading.Lock()

            def check_proxy(proxy_host, cloudfront_request):
                try:
                    # Estabelecer conexão com o proxy HTTP
                    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    proxy_socket.settimeout(0.5)  # Limite de tempo de 0.5 segundo
                    proxy_socket.connect((proxy_host, 80))  # Tentar conectar ao proxy

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
                    else:
                        color = Fore.RED
                        message = "OFFLINE"

                    # Bloquear o acesso ao print para garantir a exibição correta
                    with print_lock:
                        # Exibir a execução do proxy com a cor e mensagem adequadas
                        print(f"{color}- {message} Status: {status_code.decode()} --> {proxy_host} ")

                    # Salvar apenas os status 101 e 403 no arquivo proxy_status.txt
                    if status_code in [b'101', b'403']:
                        with open("proxy_status.txt", "a") as file:
                            file.write({proxy_host},"\n")
                    
                    
                    # Fechar a conexão com o proxy
                    proxy_socket.close()

                except Exception as e:
                    # Bloquear o acesso ao print para garantir a exibição correta
                    with print_lock:
                        # Exibir a execução do proxy com cor vermelha (erro)
                        print(f"{Fore.RED}- OFFLINE {proxy_host}")

            cloudfront_host1 = input("Informe a cloudfront/cloudflare: ")

            # Ler hosts a partir do arquivo hosts.txt
            with open("hosts.txt", "r") as file:
                hosts = file.read().splitlines()

            # Requisição a ser enviada ao CloudFront
            cloudfront_request = f"GET / HTTP/1.1\r\nHost: {cloudfront_host1}\r\nConnection: Upgrade\r\nUpgrade: Websocket\r\n\r\n"

            # Exemplo de uso com ThreadPoolExecutor
            start_time = time.time()
            with ThreadPoolExecutor() as executor:
                futures = []
                for proxy_host in hosts:
                    futures.append(executor.submit(check_proxy, proxy_host, cloudfront_request))

                # Aguardar a conclusão das tarefas
                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        print("Erro durante a execução do teste")

            execution_time = time.time() - start_time
            print("Tempo:", execution_time)
            input("Pressione Enter para continuar...")
            
############################################################################################################################  
        
        elif choice == '3':
            clear_screen()

            init(autoreset=True)

            cloudfront_host = input("Informe a cloudfront/cloudflare: ")
            cloudfront_host2 = input("Informe a sni desejada: ")
            ASA = int(input("Informe a quantidade de max_threads desejada: "))
            tmp = int(input("Informe a quantidade de segundos: "))

            # Tempo limite em segundos para a conexão
            TIMEOUT = tmp

            print_lock = threading.Lock()

            def check_proxy(proxy_host, cloudfront_host):
                try:
                    # Estabelecer conexão com o proxy TLS/SSL
                    context = ssl.create_default_context()
                    context.check_hostname = False
                    context.verify_mode = ssl.CERT_NONE
                    with socket.create_connection((proxy_host, 443), timeout=TIMEOUT) as sock:
                        with context.wrap_socket(sock, server_hostname=cloudfront_host) as sslsock:
                            # Enviar a requisição GET com o valor de CLOUDFRONT
                            request = f"GET / HTTP/1.1\r\nHost: {cloudfront_host}\r\nConnection: Upgrade\r\nUpgrade: Websocket\r\n\r\n"
                            sslsock.sendall(request.encode())

                            # Receber a resposta do proxy
                            response = sslsock.recv(4096)

                    # Coletar o número do status HTTP
                    status_code = response.split(b' ')[1]

                    # Bloquear o acesso ao print para garantir a exibição correta
                    with print_lock:
                        # Salvar apenas o status 200 no arquivo proxy_status.txt e exibir como amarelo
                        if status_code == b'200':
                            with open("proxy_status.txt", "a") as file:
                                file.write(f"Proxy: {proxy_host}, Status: {status_code.decode()}\n")
                            print(f"{Fore.YELLOW}- ONLINE - Passou perto - Proxy: {proxy_host}")
                        # Salvar os status 101 e 403 no arquivo proxy_status.txt e exibir como verde
                        elif status_code in [b'101', b'403']:
                            with open("proxy_status.txt", "a") as file:
                                file.write(f"{proxy_host}\n")
                            print(f"{Fore.GREEN}- ONLINE - {status_code.decode()} Proxy: {proxy_host}")
                        # Exibir como offline para os outros casos
                        else:
                            print(f"{Fore.RED}- OFFLINE {proxy_host}")

                except Exception as e:
                    # Bloquear o acesso ao print para garantir a exibição correta
                    with print_lock:
                        # Exibir a execução do proxy com cor vermelha (erro)
                        print(f"{Fore.RED}- OFFLINE {proxy_host}")

            # Ler hosts a partir do arquivo hosts.txt
            with open("hosts.txt", "r") as file:
                hosts = file.read().splitlines()

            # Exemplo de uso com ThreadPoolExecutor
            start_time = time.time()

            # Definir o número máximo de threads (ajuste conforme necessário)
            max_threads = ASA

            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                # Utilizar map para executar as tarefas em paralelo
                executor.map(lambda host: check_proxy(host, cloudfront_host2), hosts)

            execution_time = time.time() - start_time
            print("Tempo total de execução:", execution_time)
            
            

            input("Pressione Enter para continuar...")
            
#########################################################################################################################            
        elif choice == '4': 
            clear_screen()
            opcao = int(input("para ip aleatorias digite 1, para ips random digite 2: "))

            if opcao == 1:

                    perg =  input('digite dois grupo de 1 ip proxy \n')
                    q= int(input('intervalo 3° grupo valor menor \n'))
                    d= int(input('intervalo 3° grupo valor maior \n '))
                    
                    if perg == "":
                        perg=255
                    else:
                        perg=perg
                    
                    if q > d   :
                        q= int(input('valor menor'))
                        d= int(input('valor maior'))

                    for i in range(q, d):
                        for ii in range(1,256):
                            r= (perg+'.'+str(i)+'.'+str(ii)) 
                            print(r)
                            with open("hosts.txt", "a") as file:
                                    file.write(str(r) + "\n")

                
            elif opcao==2:
                
                qtds =int(input("informe a quantidade de ip desejado"))

                def generate_random_ip():
                    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
                    return ip

                # Exemplo de uso
                for _ in range(qtds):
                    ip = generate_random_ip()
                    print(ip)
                    with open("hosts.txt", "a") as file:
                        file.write(ip+"\n")
                        

            input("Pressione Enter para continuar...")   
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")
        
if __name__ == '__main__':
    main()
