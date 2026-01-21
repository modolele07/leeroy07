import os
import discord
from discord.ext import commands
from datetime import datetime
import pytz

INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=INTENTS)

PARIS = pytz.timezone("Europe/Paris")

ALLIANCE_NAME = "SUPERBEUZ"

MATCHMAKING = {
    "player_level": 217.50,
    "hq_level": 7.31,
    "war_points": 27738
}

ALLIANCES = [
    "bu4r","ATOMIC POWER","alpha","BELICO EL ASUNTO","GUERREROS DRAGON",
    "Tilin and friends2","Starling Vibes","ABSOLUTE VICTORY","holoX",
    "Elysian Seraphim","Celestial Dominion","LOS PIBES","Poland figthers",
    "Luxure Culinaire","Snow Bunny","MagnusDarke","JEUX-FR","NoSkill",
    "Mistic Falls","OAA","Polska Bitwa","Winged Hussars","Azgeda",
    "MAXIMUS LEVEL","BMU Reborn","Bobki","Galaxy Cowboys","I paguri",
    "Radiance","CUFFED_SQUAD","GUERREROX","Galaxy Nightmare","United Stars",
    "FALLEN ANGELS","CROATIA WARRIORS","SABER OF XEBEC","WAR GAME",
    "Shadow Nova","GALACTIC DOMINION","France Leader II","OnlyWar",
    "LOS INCONFORMITAS","Pinoy Warriors","GALAXY SPARTAN","ARCANGELES",
    "Austria Kings","CANDY KISS","XxDEPREDADORESMAXx","PRADAGAMER",
    "GalaxyWolf","THE REVOLUTION","--THE DARK SIDE--","GODS OF THE GALAXY",
    "Serbia Alliance","Sharingan"
]

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")

@bot.slash_command(name="attaquables", description="Afficher les alliances attaquables")
async def attaquables(ctx):
    embed = discord.Embed(
        title="⚔️ Alliances attaquables",
        description=f"Matchmaking de **{ALLIANCE_NAME}**",
        color=0x00ff00
    )
    for a in ALLIANCES[:15]:
        embed.add_field(name=a, value="🕒 Calcul en cours", inline=False)

    await ctx.respond(embed=embed)

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
