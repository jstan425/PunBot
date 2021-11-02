import random
import disnake

from disnake.ext import commands
from disnake.ext.commands import Param
from rich.traceback import install

install(show_locals=True)

class WisdomBall(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
    @commands.slash_command(description="Get 8ball some wisdom.")
    async def eightball(self,
                        inter,
                        question=Param(desc="Question you wish to know from 8ball.")):
             
        possible_response=[
            'Definitely',
            'There is possible',
            'Too hard to tell',
            'It is not looking good',
            'That is solid NO',
            'You gotta to be kidding, of course is YES!',
            '...',
            'No where close to YES',
            'Sorry what is the question again?',
        ]
        answer=random.choice(possible_response)
        embed=disnake.Embed(
            title="The future says...",
            description=f"{answer}",
            color=0x3fff0a
        )
        await inter.response.send_message(embed=embed)
    