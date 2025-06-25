import socket
import os
import mimetypes
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8080
DOCUMENT_ROOT = './www'

def get_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type or 'application/octet-stream'

def log(method, path, status):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {method} {path} -> {status}")

def build_response(status_code, body=b"", content_type="text/html"):
    reason = {
        200: "OK",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
    }.get(status_code, "Unknown")

    headers = (
        f"HTTP/1.1 {status_code} {reason}\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"Connection: close\r\n"
        "\r\n"
    )
    return headers.encode() + body

def read_http_request(client_socket):
    client_socket.settimeout(1)
    data = b""
    try:
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            data += chunk
            if b"\r\n\r\n" in data:
                break
    except socket.timeout:
        pass
    return data.decode(errors="ignore")

def handle_client(client_socket):
    try:
        request = read_http_request(client_socket)
        if not request:
            return

        request_line = request.splitlines()[0]
        parts = request_line.split()

        if len(parts) < 2:
            return

        method, path = parts[0], parts[1]

        if method != 'GET':
            response = build_response(405, b"<h1>405 Method Not Allowed</h1>", "text/html")
            client_socket.sendall(response)
            log(method, path, 405)
            return

        if path == '/':
            path = '/index.html'

        requested_path = os.path.normpath(os.path.join(DOCUMENT_ROOT, path.lstrip('/')))
        abs_document_root = os.path.abspath(DOCUMENT_ROOT)
        abs_requested_path = os.path.abspath(requested_path)

        # Protezione contro il path traversal
        if not abs_requested_path.startswith(abs_document_root):
            response = build_response(403, b"<h1>403 Forbidden</h1>", "text/html")
            client_socket.sendall(response)
            log(method, path, 403)
            return

        if os.path.isfile(requested_path):
            with open(requested_path, 'rb') as f:
                content = f.read()
            mime_type = get_mime_type(requested_path)
            response = build_response(200, content, mime_type)
            client_socket.sendall(response)
            log(method, path, 200)
        else:
            error_page = os.path.join(DOCUMENT_ROOT, '404.html')
            if os.path.isfile(error_page):
                with open(error_page, 'rb') as f:
                    content = f.read()
                response = build_response(404, content, "text/html")
            else:
                response = build_response(404, b"<h1>404 Not Found</h1>")
            client_socket.sendall(response)
            log(method, path, 404)

    finally:
        client_socket.close()

def start_server():
    if not os.path.isdir(DOCUMENT_ROOT):
        print(f"Errore: la directory '{DOCUMENT_ROOT}' non esiste.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            server.bind((HOST, PORT))
        except OSError as e:
            print(f"Errore durante il bind su {HOST}:{PORT} -> {e}")
            return
        server.listen(5)
        print(f"Server HTTP avviato su http://{HOST}:{PORT}/")

        while True:
            client_conn, _ = server.accept()
            handle_client(client_conn)

if __name__ == '__main__':
    start_server()
