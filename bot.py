import os
import discord
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Configurações do Discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print(f"✅ Bot conectado como {client.user}")

# HTTP Handler para enganar o Render
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Bot is running!')
        except Exception as e:
            print(f"Erro no HTTP server: {e}")

def run_http_server():
    try:
        port = int(os.environ.get("PORT", 10000))
        server = HTTPServer(('0.0.0.0', port), SimpleHandler)
        print(f"🌐 Servidor HTTP ouvindo na porta {port}")
        server.serve_forever()
    except Exception as e:
        print(f"❌ Falha ao iniciar servidor HTTP: {e}")

# Inicia o servidor HTTP em uma thread
threading.Thread(target=run_http_server, daemon=True).start()

# Inicia o bot do Discord
client.run(TOKEN)
