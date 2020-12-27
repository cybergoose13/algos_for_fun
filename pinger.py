from pythonping import ping

def ping_local_network():
    for ip in range(0,255):
        response= ping(f'192.168.1.{ip}', True)
        print(response)

ping_local_network()