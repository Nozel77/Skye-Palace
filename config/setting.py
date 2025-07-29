from dotenv import load_dotenv
import os

load_dotenv()

discordToken = os.getenv("DISCORD_BOT_TOKEN")
announcementChannelId = int(os.getenv("ANNOUNCEMENT_CHANNEL_ID"))
