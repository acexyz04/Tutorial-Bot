import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot ist bereit! Eingeloggt als {bot.user} (ID: {bot.user.id})")



@bot.event
async def on_member_join(member):
    channel = bot.get_channel(CHANNEL_ID)

    embed = discord.Embed(
        title="Willkommen auf dem Server!",
        description=(f"Hallo {member.mention}! \n\n"
        "Schön, dass du dabei bist. Lies dir die Regeln durch "
        "und habe viel Spaß auf unserem Server!"
        ),
        color = discord.Color.blurple()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.add_field(
        name = "Mitglied",
        value = member.name,
        inline = True
    )

    embed.add_field(
        name = "Mitglieder",
        value = str(member.guild.member_count),
        inline = True
    )

    embed.set_footer(
        text=f"User ID: {member.id}"
    )

    await channel.send(embed=embed)


bot.run(TOKEN)
