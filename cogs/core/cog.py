import disnake
import logging

from disnake.ext import commands

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
        embed = disnake.Embed(
            title="Reloaded!",
            description="Cogs is now reloaded",
            color=disnake.color.green(),
            )
        await inter.response.send_message(embed=embed)
        
def setup(bot:commands.Bot):
    bot.add_cog(Core(bot))
    print("Core cogs is now loaded.\n")
    
