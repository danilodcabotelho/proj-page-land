# Subindo um servidor http local com python para servidr os arquivos que estão na pasta.
# O sistema normalmente vai buscar o arquivo index.html

import os
from pathlib import Path

# Para levantar o servidor http.server do python, com mais controles
from http.server import SimpleHTTPRequestHandler, HTTPServer

#os.system('python -m http.server 3333')    Este código já levantaria o servidor python. 

host = 'localhost'
port = 3333

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f'Servidor HTTP rodando em http://{host}:{port}')
server.serve_forever()
