import random
import disnake

from disnake.ext import commands
from disnake.ext.commands import Param
from utils.formatter import generate_embed

class WisdomBall(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
    @commands.slash_command(description="Get 8ball some wisdom.")
    async def eightball(self,
                        inter,
                        question=Param(desc="Question you wish to know from 8ball.")):
             
        possible_response=[
            'Certainly, who are you kidding to?',
            'Without a doubt',
            'YES definitely',
            'You can rely on it',
            'From my view YES, not sure for you.',
            'You gotta to be kidding, of course is YES!',
            'Come on, need an answer quick. Guess you gotta to try ask again.',
            'Ask again later',
            'Sorry what is the question again?',
            'Better not tell you now',
            'Concentrate and ask again',
            'My sources says no.',
            'Very doubtful',
        ]
        
        answer=random.choice(possible_response)
        embed=generate_embed(
            title="The future says...",
            desc=f"{answer}",
            msg_type='success'
        )
        await inter.response.send_message(embed=embed)
    