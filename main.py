import asyncio
from config.setting import discordToken
from util.bot import bot
from command import announce, reactrole, welcome 

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"✅ Bot {bot.user} online! {len(synced)} slash command tersinkron.")
    except Exception as e:
        print(f"❌ Gagal sync command: {e}")

async def main():
    await announce.setup(bot)
    await reactrole.setup(bot)
    await welcome.setup(bot)
    await bot.start(discordToken)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("❌ Bot dihentikan.")
