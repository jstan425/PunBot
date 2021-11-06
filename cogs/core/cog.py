import disnake
import os
import logging

from disnake.ext import commands
from disnake.ext.commands import Param
from utils.formatter import generate_embed
from .git import Git

from rich.traceback import install
install(show_locals=True)

logger = logging.getLogger("punbot")

class Core(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
           
    @commands.slash_command(description="Prints latency of the bot between server and the host.")
    async def latency(self, inter):
        embed = generate_embed(
            title="Latency",
            desc=(f"The latency is {round(self.bot.latency * 1000)}ms"),
            msg_type= 'info'
            )
        await inter.response.send_message(embed=embed)
    
    @commands.slash_command(description="Reload Cogs")
    async def reload(self, inter):
        for folder in os.listdir("cogs"):
            if os.path.exists(os.path.join("cogs", folder, "cogs.py")):
                self.bot.unload_extension(f"cogs.{folder}.cog")
                self.bot.load_extension(f"cogs.{folder}.cog")
        embed = generate_embed(
            title="Reloaded!",
            desc="Cogs is now reloaded",
            msg_type='success',
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
    
       