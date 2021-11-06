import disnake
import logging
import os

from enum import Enum
from disnake.ext import commands
from disnake.ext.commands import Param
from utils import check
from utils.formatter import generate_embed
from github import Github
from dotenv import load_dotenv

from rich.traceback import install

install(show_locals=True)
logger = logging.getLogger("punbot")


class Git(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
    class IssueType(str, Enum):
        Bug = "bug"
        Documentation = "documentation"
        Enchancement = "enhancement"
        NeedHelp = "help wanted"
        Question = "question"
        CantFix = "wontfix"
        
    
    @commands.slash_command()
    @check.is_admin()
    async def git(self, inter):
        if inter.guild.id not in [872470314171392001, 405738567902429244]:
            embed = generate_embed(
                title="Error",
                desc="Not permitted to create issue",
                msg_type="error"
                )
            await inter.response.send_message(embed=embed)
            return
        return False
    
    @git.sub_command_group(description="List issues in the repository")
    async def issues(self, inter):
        load_dotenv()
        g = Github(os.getenv("GITTOKEN"))
        repo = g.get_repo("jstan425/PunBot")
        
        open_issues = repo.get_issues(state='open')
        for issue in open_issues:
            await inter.response.send_message(issue)
              
    @issues.sub_command(description="Create issues in repo")
    async def create(self, inter,
                  title: str= Param(desc="Title"),
                  issue_label: IssueType = Param(desc="Bugs or Enhancements"),
                  description: str= Param(None, desc="Description"),
    ):  
        
        load_dotenv()
        g = Github(os.getenv("GITTOKEN"))
        repo = g.get_repo("jstan425/PunBot")
        label = repo.get_label(issue_label)
        g = repo.create_issue(
            title=title,
            labels=[label],
            body=f"{description}" + "\n\n Raised by " + inter.author.name,
        )
        embed= generate_embed(
            title="Thank You!",
            desc="The issue had been raised successfully. You can view it at " + g.html_url,
            msg_type='success'
            )
        await inter.response.send_message(embed=embed)
