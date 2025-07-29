import discord
from discord import app_commands
from discord.ext import commands

class ReactRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_message_map = {}

    @app_commands.command(name="reactrole", description="Buat react role dengan emoji bebas")
    @app_commands.describe(
        channel="Channel tempat pesan dikirim",
        message="Pesan yang ingin ditampilkan",
        emoji="Emoji yang digunakan untuk memberi role",
        role="Role yang diberikan jika user mereaksi dengan emoji"
    )
    async def reactrole(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel,
        message: str,
        emoji: str,
        role: discord.Role
    ):
        embed = discord.Embed(
            title=message,
            color=discord.Color.blurple()
        )
        msg = await channel.send(embed=embed)
        await msg.add_reaction(emoji)

        self.role_message_map[msg.id] = {emoji: role}
        await interaction.response.send_message(f"✅ Pesan react role dikirim ke {channel.mention}.", ephemeral=True)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return 

        if payload.message_id in self.role_message_map:
            guild = self.bot.get_guild(payload.guild_id)
            role = self.role_message_map[payload.message_id].get(str(payload.emoji))
            if role:
                try:
                    member = await guild.fetch_member(payload.user_id)
                    if role not in member.roles:
                        await member.add_roles(role, reason="React role emoji")
                except Exception as e:
                    print(f"❌ Gagal menambah role: {e}")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return

        if payload.message_id in self.role_message_map:
            guild = self.bot.get_guild(payload.guild_id)
            role = self.role_message_map[payload.message_id].get(str(payload.emoji))
            if role:
                try:
                    member = await guild.fetch_member(payload.user_id)
                    if role in member.roles:
                        await member.remove_roles(role, reason="React role emoji removed")
                except Exception as e:
                    print(f"❌ Gagal menghapus role: {e}")

async def setup(bot):
    await bot.add_cog(ReactRole(bot))
