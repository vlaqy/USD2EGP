import asyncio
import discord
import requests

intents = discord.Intents()
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)
CHANNEL_ID = channel_id_here #replace this with the free api u get on apilayer.com

async def update_exchange_rate():
    channel = client.get_channel(CHANNEL_ID)

    # Send a request to the API to get the exchange rate
    url = "https://api.apilayer.com/currency_data/live?source=USD&currencies=EGP"
    api_key = "" #Api key here apilayer.com
    headers = {
        "apikey": api_key
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()

    if data["success"]:
        exchange_rate = data["quotes"]["USDEGP"]
        await channel.send(f"1 USD = {exchange_rate:.2f} EGP")


@client.event
async def on_ready():
   
    await client.change_presence(status=discord.Status.dnd)
    
    # loop this lol
    while True:
        await update_exchange_rate()
        # Wait for one day before updating the exchange rate again (We don't wanna send the same price every 2 seconds)
        await asyncio.sleep(86400)
        

client.run("")#bot token here
