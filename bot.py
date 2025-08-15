from flask import Flask
import threading
import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz
import os

# =========================
# Configuração do Discord
# =========================
TOKEN = os.environ["TOKEN"]
GUILD_ID = int(os.environ["GUILD_ID"])
CHANNEL_ID = int(os.environ["CHANNEL_ID"])
ROLE_ID = int(os.environ["ROLE_ID"])

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def enviar_mensagem(evento):
    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        print("[ERRO] Servidor não encontrado.")
        return False
    canal = guild.get_channel(CHANNEL_ID)
    if canal is None:
        print("[ERRO] Canal não encontrado.")
        return False
    role = guild.get_role(ROLE_ID)
    if role is None:
        print("[ERRO] Cargo não encontrado.")
        return False
    try:
        await canal.send(f"{role.mention} {evento}")
        print(f"[DEBUG] Mensagem enviada: {evento}")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao enviar mensagem: {e}")
        return False

@tasks.loop(minutes=1)
async def agendar_mensagens():
    tz = pytz.timezone("America/Sao_Paulo")
    hora_atual = datetime.now(tz).strftime("%H:%M")
    eventos = {
        "12:55": "EVENTO PVP",
        "18:55": "BOSS RYUKUDDOU",
        "19:55": "EVENTO PVP"
    }
    if hora_atual in eventos:
        await enviar_mensagem(eventos[hora_atual])

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    agendar_mensagens.start()

# =========================
# Comando manual de teste
# =========================
@bot.command()
async def teste(ctx, *, evento="TESTE MANUAL"):
    enviado = await enviar_mensagem(evento)
    if enviado:
        await ctx.send(f"✅ Mensagem de teste enviada: {evento}")
    else:
        await ctx.send("❌ Erro ao tentar enviar a mensagem.")


# =========================
# Servidor Flask para Web Service
# =========================
app = Flask("")

@app.route("/")
def home():
    return "Bot Discord rodando no Render Web Service!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# Rodar Flask em thread separada
threading.Thread(target=run_flask).start()

# Rodar bot Discord
bot.run(TOKEN)
