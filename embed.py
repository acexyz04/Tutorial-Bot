import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=f"Latency: {round(bot.latency * 1000)}ms", color=discord.Color.blue())
    await ctx.send(embed=embed)
    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run("BOT_TOKEN_HERE")
