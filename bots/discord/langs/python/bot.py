import discord

TOKEN = None  # Replace with your bot's token

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

if __name__ == "__main__":
    if TOKEN is not None:
        client.run(TOKEN)
    else:
        print("❌ No token provided! Please set the TOKEN variable in bot.py.")
        input("Press Enter to exit...")