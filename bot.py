import os
import discord

intents = discord.Intents.default()
intents.message_content = True  # depende das permissões do seu bot
client = discord.Client(intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")

client.run(TOKEN)

