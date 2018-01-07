import requests
import discord
from discord.ext import commands

class Etherscan:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gvsupply(self):

        await self.bot.say("GVC: 100,000,000,000")

def setup(bot):
    bot.add_cog(Etherscan(bot))