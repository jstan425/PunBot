import logging
import disnake
import datetime
import humanfriendly

from disnake.ext import commands
from disnake.ext.commands import Param

from utils import check
from utils.formatter import gen_embed


logger = logging.getLogger("punbot/ Admin")

class Admin(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.slash_command(description="Kick a user")
    @check.is_mod()
    async def kick(self,
            inter,
            user: disnake.User=Param(desc="Specify a user."),
            reason: str=Param(None, desc="Reason to be kicked."),
        ):

        embed = gen_embed(
            title="Uh-oh..!",
            desc=f'{user.name}had been kicked for {reason}',
            msg_type='warning',
        )

        await disnake.guild.kick(reason=reason)
        await inter.response.send_message(embed=embed)
    
    @commands.slash_command(description="Timeout a user")
    @check.is_mod()
    async def timeout(self,
            inter,
            user: disnake.User=Param(desc="Specify a user"),
            duration = Param(desc="Duration to be timeout"),
            reason = Param(None, desc="Reason to be timeout")
        ):
        # Timeout a member for specific time. 
        # Use 5m for 5 mins, 1hr for 1 hour etc.
        if reason is None:
            reason = 'No reason provided'
        duration = humanfriendly.parse_timespan(duration)
        embed = gen_embed(
            title="Uh-oh..!",
            desc=f'{user.name} had been timeout for {duration}. \nReason: {reason}',
            msg_type='warning',
        )
        try:
            await disnake.Guild.timeout(self, user=user, until=disnake.utils.utcnow() + datetime.timedelta(seconds=duration), reason=reason)
            await inter.response.send_message(embed=embed)
        except disnake.HTTPException as e:
            await inter.response.send_message("Timeout failed, please contact admin.")
            
def setup(bot:commands.Bot):
    bot.add_cog(Admin(bot))
    print("Admin cog is now loaded.\n")
    logger.info("Admin cog loaded")


def teardown(bot:commands.Bot):
    bot.remove_cog(Admin(bot))
    print("Admin cogs is now unloaded.\n")
    logger.info("Admin cog unloaded")


