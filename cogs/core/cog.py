import disnake
import os
import logging

from disnake.ext import commands
from disnake.ext.commands import Param
from utils import check
from .git import Git

from rich.traceback import install
install(show_locals=True)

logger = logging.getLogger("punbot")

class Core(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
           
    @commands.slash_command(description="Prints latency of the bot between server and the host.")
    async def latency(self,
                      inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(
            title="Latency",
            description=(f"The latency is {round(self.bot.latency * 1000)}ms"),
            color=disnake.Color.blue(),
            )
        await inter.response.send_message(embed=embed)
    
    @commands.slash_command(description="Reload Cogs")
    async def reload(self,
                     inter: disnake.ApplicationCommandInteraction):
        for folder in os.listdir("cogs"):
            if os.path.exists(os.path.join("cogs", folder, "cogs.py")):
                self.bot.unload_extension(f"cogs.{folder}.cog")
                self.bot.load_extension(f"cogs.{folder}.cog")
        embed = disnake.Embed(
            title="Reloaded!",
            description="Cogs is now reloaded",
            color=0x3fff0a,
            )
        await inter.response.send_message(embed=embed)
        print("Cogs is now reloaded.")
        logger.info("Cogs Reloaded")
    
        
def setup(bot:commands.Bot):
    bot.add_cog(Core(bot))
    print("Core cog is now loaded.\n")
    logger.info("Core cog loaded")
    bot.add_cog(Git(bot))
    print("Git cog is now loaded.\n")
    logger.info("Git cog loaded")

def teardown(bot:commands.Bot):
    bot.remove_cog(Core(bot))
    print("Core cogs is now unloaded.\n")
    logger.info("Core cog unloaded")
    bot.remove_cog(Git(bot))
    print("Git cogs is now unloaded.\n")
    logger.info("Git cog unloaded")
    
       