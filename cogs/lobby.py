import discord
from discord.ext import commands
from config import WELCOMER, GOODBYER
class LobbyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channelId = WELCOMER.get("ChannelId")
        channel = member.guild.get_channel(channelId)
        formattedDescription = WELCOMER.get("EmbedDescription").replace("[usermention]", member.mention).replace("[membercount]", str(member.guild.member_count))
        embed = discord.Embed(
            title=WELCOMER.get("EmbedTitle"),
            description=formattedDescription,
            color=WELCOMER.get("EmbedColor")
        )
        embed.set_image(url=WELCOMER.get("EmbedImage"))
        embed.set_footer(text=WELCOMER.get("EmbedFooter"))
        await channel.send(embed=embed)
    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channelId = GOODBYER.get("ChannelId")
        channel = member.guild.get_channel(channelId)
        formattedDescription = GOODBYER.get("EmbedDescription").replace("[usermention]", member.mention).replace("[membercount]", str(member.guild.member_count))
        embed = discord.Embed(
            title=GOODBYER.get("EmbedTitle"),
            description=formattedDescription,
            color=GOODBYER.get("EmbedColor")
        )
        embed.set_image(url=GOODBYER.get("EmbedImage"))
        embed.set_footer(text=GOODBYER.get("EmbedFooter"))
        await channel.send(embed=embed)
async def setup(bot):
    await bot.add_cog(LobbyCog(bot))
