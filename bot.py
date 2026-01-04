import discord
from discord.ext import commands
import config
from utils import console_logs
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    for cog in config.ENABLED_COGS:
        try:
            await bot.load_extension("cogs."+cog)
            console_logs.colorInfo(f"Loaded module {cog} successfully")
        except Exception as e:
            console_logs.colorError(f"An error has occured: {e}")
    cmds = await bot.tree.sync()
    for cmd in cmds:
        console_logs.colorInfo(f"Synchronized command {cmd} sucessfully")
    console_logs.colorInfo(f"A total of {len(cmds)} commands has been synchronized")
    activity = discord.Activity(type=discord.ActivityType.listening, name=config.BASIC.get("StatusContent"))
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    console_logs.colorInfo("Bot initialization has been completed")
    console_logs.colorInfo(f"Logged in as {bot.user.name}#{bot.user.discriminator}")
bot.run(config.TOKEN)