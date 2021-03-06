import disnake
import logging
import os

from enum import Enum
from disnake.ext import commands
from disnake.ext.commands import Param
from utils import check
from utils.formatter import gen_embed
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
            embed = gen_embed(
                title="Error",
                desc="Not permitted to create issue",
                msg_type="error"
                )
            await inter.response.send_message(embed=embed)
            return
        return False
    
    @git.sub_command_group()
    async def issues(self, inter):
        return

    @issues.sub_command(description="Submit issue that required attention.")
    async def create(self, 
                inter,
                title: str= Param(desc="Describe the title of the issue."),
                issue_label: IssueType = Param(desc="Label for the issue."),
                description: str= Param(None, desc="Describe the issue in detailed (if possible)."),
    ):  
        
        load_dotenv()
        g = Github(os.getenv("GITTOKEN"))
        repo = g.get_repo("jstan425/PunBot")
        label = repo.get_label(issue_label)
        g = repo.create_issue(
            title=title,
            labels=[label],
            body=f"{description}" + "\n\n by: " + inter.author.name,
        )
        embed= gen_embed(
            title="Thank You!",
            desc="The issue had been raised successfully. You can view it at " + g.html_url,
            msg_type='success'
            )
        await inter.response.send_message(embed=embed)

    @issues.sub_command(description="Print the issue(s) list from repo.")
    async def list(self, inter):
        load_dotenv()
        g = Github(os.getenv("GITTOKEN"))
        repo = g.get_repo("jstan425/PunBot")
        
        open_issues = repo.get_issues(state="open")
        embed = gen_embed(title="List of issues in the repo.", msg_colour=0x7818af)
        await inter.response.send_message(embed=embed)
        for issue in open_issues:
            embed.add_field(
                name='Issue #' + str(issue.number) + ' - ' + str(issue.title) + ' (' + str(issue.labels[0].name) + ')',
                value= str(issue.body) + '\n**Permalink**: ' + str(issue.html_url),
                inline = False
                )
        await inter.edit_original_message(embed=embed)
    
    @issues.sub_command(description="Add comments to a issue.")
    async def add(self, inter,
            issue_id: int=Param(desc="ID of the issue that need to be commented."),
            comment: str=Param(desc="Description that need to be add on.")
            ):
            
        load_dotenv()
        g = Github(os.getenv("GITTOKEN"))
        repo = g.get_repo("jstan425/PunBot")

        issue= repo.get_issue(number=int(issue_id))
        comments= issue.create_comment(str(comment))

        embed = gen_embed(
            title="Comment added successfully to the issue",
            msg_type="success",
            desc="Your comment is now viewable at " + issue.html_url
        )
        await inter.response.send_message(embed=embed)
