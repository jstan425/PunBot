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
                        question=Param(None, desc="Ask me a wisdom question, to get a wisdom answer.")):
        possible_response=[
            'Definitely',
            'There is possible',
            'Too hard to tell',
            'It is not looking good',
            'That is solid NO'
        ]
        await inter.response.send_message(random.choice(possible_response) + ", " + disnake.Message.mentions)
    