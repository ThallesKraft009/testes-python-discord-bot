import nextcord
from nextcord.ext import commands



class Slash(commands.Cog, name="SlashCommands"):
    def __init__(self, pudim: commands.Bot):
        self.bot = pudim

    @nextcord.slash_command(description="Veja minha latência")
    async def ping(self, interaction: nextcord.Interaction):
        await interaction.send(f"🏓 Pong {round(self.bot.latency * 1000)}ms")
      

    @nextcord.slash_command(description="Faça eu enviar sua msg")
    async def say(self, interaction: nextcord.Interaction, msg: str):
      await  interaction.response.send_message(f"Enviei a msg.", ephemeral=True)
      chat = interaction.channel
      await chat.send(msg)


def setup(pudim: commands.Bot):
    pudim.add_cog(Slash(pudim))
