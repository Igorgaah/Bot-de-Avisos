import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz
import os  # Para pegar variáveis de ambiente

# Configurações via variáveis de ambiente
TOKEN = os.environ["TOKEN"]  # Token do bot
GUILD_ID = int(os.environ["GUILD_ID"])  # ID do servidor
CHANNEL_ID = int(os.environ["CHANNEL_ID"])  # ID do canal
ROLE_ID = int(os.environ["ROLE_ID"])  # ID do cargo

# Intents
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
        print("[DEBUG] Mensagem enviada com sucesso!")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao enviar mensagem: {e}")
        return False


@tasks.loop(minutes=1)
async def agendar_mensagens():
    tz = pytz.timezone("America/Sao_Paulo")
    hora_atual = datetime.now(tz).strftime("%H:%M")
    print(f"[DEBUG] Hora atual SP: {hora_atual}")

    eventos = {
        "12:55": "EVENTO PVP",
        "18:55": "BOSS RYUKUDDOU",
        "19:55": "EVENTO PVP"
    }

    if hora_atual in eventos:
        print(f"[DEBUG] Horário bateu! Evento: {eventos[hora_atual]}")
        await enviar_mensagem(eventos[hora_atual])


# Comando manual de teste
@bot.command()
async def teste(ctx, *, evento="TESTE MANUAL"):
    enviado = await enviar_mensagem(evento)
    if enviado:
        await ctx.send(f"✅ Mensagem de teste enviada: {evento}")
    else:
        await ctx.send("❌ Erro ao tentar enviar a mensagem.")


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    print("Iniciando agendamento de mensagens...")
    agendar_mensagens.start()


bot.run(TOKEN)
