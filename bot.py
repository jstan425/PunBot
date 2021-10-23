import logging
import os
import platform
from logging.handlers import TimedRotatingFileHandler

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

if os.name != "nt":
    import uvloop

    uvloop.install()

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

    logger = logging.getLogger("disnake")
    logger.setLevel(logging.INFO)
    log_dir = "logs"
    handler = TimedRotatingFileHandler(
        os.path.join(log_dir, "punbot.log"), when="midnight", interval=1, backupCount=5
    )
    handler.suffix = "%Y-%m-%d_%H-%M-%S"
    handler.setFormatter(
        logging.Formatter("%(ascitime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)
    return logger


logger = setup_logging()
print("Cogs Loading..." + "\n")
for folder in os.listdir("cogs"):
    if os.path.exists(os.path.join("cogs", folder, "cog.py")):
        bot.load_extension(f"cogs.{folder}.cog")

print("Cogs Loaded" + "\n")
logger.info("Bot Started")
bot.run(os.getenv("TOKEN"))
logger.info("--------Bot Started--------")
