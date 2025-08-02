import discord
from discord.ext import commands
from config.setting import channelId

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_channel_id = channelId

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(self.welcome_channel_id)
        if channel is None:
            return

        await channel.send(f"Holaaa, {member.mention}!")

        embed = discord.Embed(
            title="🪩 WELCOME TO SKYE PALACE! 🪩",
            description=(
                "• REACT DI `#⁠👉┋𝑻𝑨𝑲𝑬-𝑹𝑶𝑳𝑬` UNTUK MENGAMBIL ROLE\n"
                "• VVIP, ROYAL, DAN TEXT DI SCREEN SILAHKAN OPEN TICKET DI `#🎟️┋𝑶𝑷𝑬𝑵-𝑻𝑰𝑪𝑲𝑬𝑻`\n"
                "• UNTUK BANTUAN CHAT DI `#🚩┋𝑯𝑬𝑳𝑷`"
            ),
            color=discord.Color.blue()
        )

        file = discord.File("assets/welcome.png", filename="welcome.png")
        embed.set_image(url="attachment://welcome.png")

        await channel.send(file=file, embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))
