import discord
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.tree.command(
    name="v2_demo",
    description="Demo for the new Discord UI components"
)
async def v2_demo(interaction: discord.Interaction):
    container = discord.ui.Container(
        discord.ui.TextDisplay(
            "# Components V2 Container"
        ),

        discord.ui.Separator(),

        discord.ui.Section(
            discord.ui.TextDisplay(
                "## Struktur basiert auf Container\n"
                "Text, Sections und Layout werden direkt kombiniert.\n"
                "Alles wird von Discord als UI gerendert."
            ),
            accessory=discord.ui.Thumbnail(interaction.user.display_avatar.url)
        ),

        discord.ui.Separator(),

        discord.ui.TextDisplay(
            "-# Demo ohne interaktionen - nur UI Aufbau"
        )
    )

    view = discord.ui.LayoutView()
    view.add_item(container)

    await interaction.response.send_message(
        view=view,  
    )

bot.run(TOKEN)
