import socketio

client_socket = None


def initialize_socket(host: str = "b2ml_api_test", port: int = 5643):
    """Inicializa o socket globalmente."""
    global client_socket
    if client_socket is None:
        try:
            client_socket = socketio.Client()
            client_socket.connect(f"http://{host}:{port}")
        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")
            client_socket = None


def send_api_message(event, msg):
    """Envia uma mensagem para o servidor."""
    global client_socket
    if client_socket is None:
        initialize_socket()  # Tente inicializar o socket

    if client_socket:
        try:
            client_socket.emit(event, msg)
        except Exception as e:
            print(f"Erro ao enviar a mensagem: {e}")
    else:
        print("Cliente Socket.IO não está conectado.")
