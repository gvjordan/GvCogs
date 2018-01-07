import discord
import requests
from discord.ext import commands

class etherscan:

    def __init__(self, bot)
        self.bot = bot

    @commands.command()
    async def gvcoinsuspply(self):
    	# TEST
        await self.bot.say("GVCOIN: 100,000,000,000")

def setup(bot):
    bot.add_cog(etherscan(bot))