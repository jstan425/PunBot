import logging

from disnake.ext import commands
from rich.traceback import install
from .eightball import WisdomBall


install(show_locals=True)
logger = logging.getLogger("punbot")

def setup(bot: commands.Bot):
    bot.add_cog(WisdomBall(bot))
    print("Fun cog is now loaded\n")
    logger.info("Fun cog loaded successfully")
    
def teardown(bot: commands.Bot):
    bot.remove_cog(WisdomBall(bot))
    print("Fun cog is now unloaded\n")
    logger.info("Fun cog unloaded successfully")
    