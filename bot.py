import os
import asyncio
import nextcord
from nextcord.ext import commands

TOKEN = "seu token"
PREFIXO = "Seu prefixo"

def main():
    intents = nextcord.Intents.default()

    intents.message_content = True
    intents.guilds = True
    intents.members = True




    status = nextcord.Activity(
        type=nextcord.ActivityType.listening, name=f"Todos vocês :D"
    )

    pudim = commands.Bot(
        commands.when_mentioned_or(PREFIXO),
        intents=intents,
        activity=status,
    )

    
    
    for folder in os.listdir("cogs"):
        pudim.load_extension(f"cogs.{folder}")

    @pudim.listen()
    async def on_ready():
        assert pudim.user is not None
        print(f"To online em {pudim.user.name} ")

    
    pudim.run(TOKEN)


if __name__ == "__main__":
    main()
