from dotenv import load_dotenv
import os

load_dotenv()

discordToken = os.getenv("DISCORD_BOT_TOKEN")
channelId = int(os.getenv("CHANNEL_ID"))
take_role_channel = int(os.getenv("TAKE_ROLE_CHANNEL_ID"))
open_ticket_channel = int(os.getenv("OPEN_TICKET_CHANNEL_ID"))
help_channel = int(os.getenv("HELP_CHANNEL_ID"))
