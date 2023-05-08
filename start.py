# Импорт библиотек для запуска Web-сервера
from http.server import HTTPServer, CGIHTTPRequestHandler

# Адрес сервера и номер порта, который он будет "слушать"
server_address = ('', 80)

# Создаем объект Web-сервер
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

# Старт Web-сервера
print('start')
httpd.serve_forever()
print('stop')
