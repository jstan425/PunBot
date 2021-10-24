import disnake
import os
import logging


from enum import Enum
from disnake.ext import commands
from disnake.ext.commands import Param
from utils import check
from github import Github
from dotenv import load_dotenv

logger = logging.getLogger("punbot")

class Core(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    class Repo(str, Enum):
        PunBot = "PunBot"
        
    class IssueType(str, Enum):
        Bug = "bug"
        Enchancement = "enhancement"
            
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
            color=disnake.Color.green(),
            )
        await inter.response.send_message(embed=embed)
    
    @commands.slash_command(description="Create issues in Repo")
    @check.is_mod()
    async def gitcreate(self,
                        inter: disnake.ApplicationCommandInteraction,
                        repo: Repo = Param(desc="Select a repo"),
                        issuetype: IssueType = Param(desc="Bugs or Enhancements"),
                        title: str= Param(desc="Title"),
                        description: str= Param(desc="Description"),
    ):
        if inter.guild.id not in [872470314171392001]:
            embed = disnake.Embed(
                title="Error",
                description="Not permitted to create issue",
                color=disnake.Color.red()
                )
            await inter.response.send_message(embed=embed)
            return
        
        load_dotenv()
        g = Github(os.getenv("GITTOKEN"))
        if repo == "PunBot": 
            repo = g.get_repo("jstan425/PunBot")
        label = repo.get_label(issuetype)
        g = repo.create_issue(
            title=title,
            labels=[label],
            body=description + "\n\nraised by: " + inter.author.name,
        )
        embed= disnake.Embed(
            title="Thank You!",
            description="Issue raised successfully via " + g.html_url,
            color=disnake.Color.green()
            )
        
        await inter.response.send_message(embed=embed)
    
def setup(bot:commands.Bot):
    bot.add_cog(Core(bot))
    print("Core cogs is now loaded.\n")

def teardown(bot:commands.Bot):
    bot.remove_cog(Core(bot))
    print("Core cogs is now unloaded.\n")
       