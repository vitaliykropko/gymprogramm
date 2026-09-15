import http.server
import socketserver
import socket
import webbrowser

PORT = 8080

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    local_ip = get_local_ip()
    print("=" * 60)
    print("  🏋️ Фитнес-приложение запущено локально!")
    print(f"  👉 На компьютере:   http://localhost:{PORT}")
    print(f"  📱 На телефоне:     http://{local_ip}:{PORT}")
    print("     (телефон должен быть подключен к тому же Wi-Fi)")
    print("=" * 60)
    print("Для остановки сервера нажмите Ctrl + C")

    webbrowser.open(f"http://localhost:{PORT}")

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер остановлен.")
