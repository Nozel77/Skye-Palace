import discord
from discord.ext import commands

class AnnounceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="announce")
    @commands.has_permissions(administrator=True)
    async def text_announce(self, ctx, channel: discord.TextChannel, *, message: str = ""):
        try:
            files = [await attachment.to_file() for attachment in ctx.message.attachments] if ctx.message.attachments else None
            await channel.send(content=message or None, files=files)
            await ctx.reply(f"✅ Pengumuman berhasil dikirim ke {channel.mention}", mention_author=False)
        except Exception as e:
            await ctx.reply(f"❌ Gagal mengirim: {e}", mention_author=False)

async def setup(bot):
    await bot.add_cog(AnnounceCommand(bot))
