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
    if message.content.startswith("!red"):
        if message.content.startswith("!red dé"):
            await client.send_message(message.channel,str(random.randint(1,6)))
        if message.content.startswith("!red rep"):
            mess = message.content.lstrip("!red rep")
            if not mess.startswith("^^") or mess.startswith("!"):
                await client.delete_message(message)
                await client.send_message(message.channel,mess)
        if message.content.startswith("!red aut"):
            await client.send_message(message.channel,message.author)

client.run("NDM4MDQ4NTkzNzc4MzExMTY4.Db_I0w.2yvvfel6n860rxPA72HHYGvYUJo")
