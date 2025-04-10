import os
import discord
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")

# Servidor HTTP falso
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running!')

def run_http_server():
    port = int(os.environ.get("PORT", 10000))  # Usa a porta que o Render define
    print(f"Servidor HTTP ouvindo na porta {port}")  # ESSA LINHA AJUDA MUITO NO DEBUG
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

# Inicia o servidor HTTP falso em uma thread separada
threading.Thread(target=run_http_server, daemon=True).start()

# Inicia o bot do Discord
client.run(TOKEN)
