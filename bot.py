import discord
import responses



async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_resposne(user_message)
        await message.channel.send(response) if is_private else await message.channel.send(reseponse)
    except Exception as e:
        print(e)
    

def run_discord_bot():
    TOKEN = "MTE1MzE3NDk0MzQ4MDE2NDQyMw.GukJ1A.RLsC7HsO7FCGzbTX7sPtoRoXeLIwaqc2p6ucVY"
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print(f"{client.user} is now running")
    
    client.run(TOKEN)