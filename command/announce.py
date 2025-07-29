import discord
from discord import app_commands
from discord.ext import commands

class AnnounceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="announce", description="Kirim pengumuman ke channel tertentu")
    @app_commands.describe(
        channel="Channel tujuan pengumuman",
        message="Isi dari pengumuman"
    )
    async def announce(self, interaction: discord.Interaction, channel: discord.TextChannel, message: str):
        try:
            await channel.send(message)
            await interaction.response.send_message(f"✅ Pengumuman berhasil dikirim ke {channel.mention}", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Gagal mengirim: {str(e)}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(AnnounceCommand(bot))
