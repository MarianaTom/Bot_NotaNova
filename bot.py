import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

ID_ASISTENCIA = 1389709699301118095
ID_UPDATE = 1389837483327488011

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Función para cargar mensajes de texto
def cargar_mensaje(nombre_archivo):
    ruta = os.path.join("recordatorios", nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

@bot.command()
async def r_avance(ctx):
    canal = bot.get_channel(ID_ASISTENCIA)
    mensaje = cargar_mensaje("mensaje_avance.txt")
    await canal.send(mensaje)
    await ctx.send("✅ Recordatorio de avance enviado.")

@bot.command()
async def r_urgente(ctx):
    canal = bot.get_channel(ID_ASISTENCIA)
    mensaje = cargar_mensaje("mensaje_avanceUrgente.txt")
    await canal.send(mensaje)
    await ctx.send("✅ Recordatorio urgente enviado.")

@bot.command()
async def r_asistencia(ctx):
    canal = bot.get_channel(ID_UPDATE)
    with open("recordatorios/JuntaSemanal.png", "rb") as f:
        imagen = discord.File(f)
    link = cargar_mensaje("asistenciaJunta.txt")
    mensaje = await canal.send("@everyone", file=imagen)
    await mensaje.reply(f"Registra tu asistencia: [Aquí]({link})")
    await ctx.send("✅ Recordatorio de asistencia enviado.")

bot.run(TOKEN)
