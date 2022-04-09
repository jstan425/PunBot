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

