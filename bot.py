import os
import discord

intents = discord.Intents.default()
intents.message_content = True  # depende das permissões do seu bot
client = discord.Client(intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running!')

def run_http_server():
    server = HTTPServer(('0.0.0.0', 10000), SimpleHandler)
    server.serve_forever()

# Inicia o servidor HTTP falso em uma thread separada
threading.Thread(target=run_http_server, daemon=True).start()

client.run(TOKEN)

