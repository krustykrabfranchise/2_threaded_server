import socket


def echo_client(host='127.0.0.1', port=60000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Connected to the server.")
        while True:
            message = input("Введите сообщение (напишите 'exit' для выхода): ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Ответ от сервера: {data.decode()}")


if __name__ == '__main__':
    echo_client()
