import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("----------")

@client.event
async def on_message(message):
    if message.content.startswith("!red dé"):
        await client.send_message(message.channel,str(random.randint(1,6)))

client.run("NDM4MDQ4NTkzNzc4MzExMTY4.Db_I0w.2yvvfel6n860rxPA72HHYGvYUJo")
