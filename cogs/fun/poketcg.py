import Disnake
import pokemontcgsdk
import os

from disnake.ext import commands
from disnake.ext.commands import Params
from utils.formatter import gen_embed 
from dotenv import load_dotenv

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity
from pokemontcgsdk import RestClient

load_dotenv()

RestClient.configure(os.getenv("X-API"))

class PokeTCG(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Get PokeTCG card")
    async def card(self, 
            inter,
            name = Param(desc="Name of the card"), 
            id=Param(None, desc="Set ID")
        ):
        # Search card based on name and Set ID
        cards = Card.where(q='set.name=name set.id=id')
        embed = gen_embed(
            title = ""
        )

    @commands.slash_command(description="Get PokeTCG card")
    async def list_sets(self, 
                        inter):
                    sets = Set.all()




