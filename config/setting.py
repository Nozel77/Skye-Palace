from dotenv import load_dotenv
import os

load_dotenv()

discordToken = os.getenv("DISCORD_BOT_TOKEN")
channelId = int(os.getenv("CHANNEL_ID"))
