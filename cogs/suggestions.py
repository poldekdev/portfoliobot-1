import discord
from discord.ext import commands
from config import SUGGESTIONS as CONFIG

class PropozycjeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        channel = message.channel
        author = message.author
        if author.bot:
            return
        if channel.id != CONFIG.get("ChannelId"):
            return
        if isinstance(channel.type, discord.Thread):
            return
        await message.delete()
        formattedDescription = CONFIG.get("EmbedDescription").replace("[author]", author.mention).replace("[content]", message.content)
        embed = discord.Embed(
            title=CONFIG.get("EmbedTitle"),
            description=formattedDescription,
            color=CONFIG.get("EmbedColor")
        )
        embed.set_image(url=CONFIG.get("EmbedImage"))
        embed.set_footer(text=CONFIG.get("EmbedFooter"))
        msg = await channel.send(embed=embed)
        await msg.add_reaction(CONFIG.get("YesReaction"))
        await msg.add_reaction(CONFIG.get("NoReaction"))
        await msg.create_thread(name="Disscution")
async def setup(bot):
    await bot.add_cog(PropozycjeCog(bot))
