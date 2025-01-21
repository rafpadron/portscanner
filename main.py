import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

# Lista de puertos comunes
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 587, 993, 995, 3306, 3389]

def scan_port(ip, port):
    # Crea un socket para conectarse al puerto especificado
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Establece un tiempo de espera de 1 segundo
    try:
        result = s.connect_ex((ip, port))  # Intenta conectarse al puerto
        if result == 0:
            print(f"Port {port} is open")  # Si la conexión es exitosa, el puerto está abierto
            try:
                banner = s.recv(1024).decode().strip()  # Intenta leer el banner
                if banner:
                    print(f"Banner: {banner}")
            except:
                print("No banner available")
        else:
            print(f"Port {port} is closed")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
    finally:
        s.close()  # Cierra el socket

def main():
    # Configura el analizador de argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("ip", help="IP address to scan")  # Dirección IP a escanear
    parser.add_argument("-p", "--ports", help="Range of ports to scan (e.g., 1-65535)", default="1-65535")  # Rango de puertos a escanear
    parser.add_argument("-t", "--threads", help="Number of threads to use", type=int, default=100)  # Número de hilos a utilizar
    parser.add_argument("-c", "--common", help="Scan common ports only", action="store_true")  # Opción para escanear solo puertos comunes
    args = parser.parse_args()

    ip = args.ip  # Obtiene la dirección IP del argumento
    num_threads = args.threads  # Número de hilos

    if args.common:
        ports_to_scan = COMMON_PORTS  # Usa la lista de puertos comunes
    else:
        port_range = args.ports.split('-')  # Divide el rango de puertos en inicio y fin
        start_port = int(port_range[0])  # Puerto inicial
        end_port = int(port_range[1])  # Puerto final
        ports_to_scan = range(start_port, end_port + 1)  # Rango de puertos a escanear

    # Crea un grupo de hilos para ejecutar el escaneo en paralelo
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for port in ports_to_scan:
            executor.submit(scan_port, ip, port)  # Envía la tarea de escanear el puerto a un hilo

if __name__ == "__main__":
    main()  # Ejecuta la función principal