import discord
from discord.ext import commands
from config.setting import channelId, take_role_channel, open_ticket_channel, help_channel

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_channel_id = channelId

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(self.welcome_channel_id)
        if channel is None:
            return
        
        embed = discord.Embed(
            title="SELAMAT DATANG DI SKYE PALACE! 🪩",
            description=(
                f"Holaaa, {member.mention}!\n\n"
                f"• REACT DI <#{take_role_channel}> UNTUK MENGAMBIL ROLE\n"
                f"• VVIP, ROYAL, DAN TEXT DI SCREEN SILAHKAN OPEN TICKET DI <#{open_ticket_channel}> \n"
                f"• UNTUK BANTUAN CHAT DI <#{help_channel}>\n\n"
                "Enjoy the party and have fun! 🪩"
            ),
        )

        file = discord.File("assets/welcome.png", filename="welcome.png")
        embed.set_image(url="attachment://welcome.png")

        await channel.send(file=file, embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))
