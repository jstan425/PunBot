import os
import platform
import logging
from logging.handlers import TimedRotatingFileHandler
from rich.traceback import install


import disnake
from disnake.ext import commands
from dotenv import load_dotenv

if os.name != "nt":
    import uvloop

    uvloop.install()

install(show_locals=True)
load_dotenv()

intents = disnake.Intents.all()
bot = commands.Bot(
    command_prefix="pb-",
    intents=intents,
    test_guilds=[872470314171392001],
    sync_commands_debug=True,
)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")
    print(f"Disnake API version: {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on {platform.system()} {platform.release()} ({os.name})")
    print("----------------------------------")


def setup_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("punbot")
    logger.setLevel(logging.DEBUG)
    log_dir = "logs"
    handler = TimedRotatingFileHandler(
        os.path.join(log_dir, "punbot.log"), when="midnight", interval=1, backupCount=5
    )
    handler.suffix = "%Y-%m-%d_%H-%M-%S"
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)
    return logger


def load_cogs(bot, logger):
    logger.info("Cogs are loading...")
    print("Cogs are Loading...\n")
    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            bot.load_extension(f"cogs.{folder}.cog")
    logger.info("Cogs are now fully loaded")
    print("Cogs are now Fully Loaded\n")


logger = setup_logging()
load_cogs(bot, logger)

logger.info("Bot Started")
bot.run(os.getenv("TOKEN"))
