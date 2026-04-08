import socket

target = input("Digite o site ou IP: ")

print(f"\nEscaneando alvo: {target}\n")
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        result = s.connect_ex((target, port))
        
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "desconhecido"
            
            print(f"Porta {port} ABERTA - Serviço: {service}")
    
    except:
        pass

    s.close()