import discord
import responses

# Define your intents
intents = discord.Intents.default()
intents.typing = False  # You can customize your intents as needed

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "MTE1MzE3NDk0MzQ4MDE2NDQyMw.GwNdVY.uEChisq1dvhFWOxDcIKQ09DQwfnZt_QviGv5AI"
    client = discord.Client(intents=intents)  # Pass the intents object
    
    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    client.run(TOKEN)