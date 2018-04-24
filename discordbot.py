import discord
import asyncio
import random
from os.path import exists
from os import remove

client = discord.Client()
version = "0.6"

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
        elif message.content.startswith("!red rep"):
            mess = message.content.lstrip("!red rep")
            if not mess.startswith("^^") and not mess.startswith("!"):
                await client.delete_message(message)
                await client.send_message(message.channel,mess)
        elif message.content.startswith("!red aut"):
            await client.send_message(message.channel,message.author)
        elif message.content.startswith("!red ver"):
            await client.send_message(message.channel,version)
        elif message.content.startswith("!red aléa"):
            dat = message.content.split(" ")
            if len(dat) != 4:
                await client.send_message(message.channel,"Erreur 1")
            else:
                try:
                    a,b = int(dat[2]), int(dat[3])
                except ValueError:
                    await client.send_message(message.channel, "Erreur 2")
                except:
                    await client.send_message(message.channel, "Erreur Inattendue")
                else:
                    if a > b:
                        a,b = b,a
                    await client.send_message(message.channel,str(random.randint(a,b)))
        elif message.content.startswith("!red mser"):
            await client.send_message(message.channel,"micrausôft sécouryti éèraure")
        elif message.content.startswith("!red testw"):
            dat = message.content.split(" ")
            if len(dat) != 4:
                await client.send_message(message.channel, "Erreur 3")
            else:
                fich = open(dat[2],"w")
                for i in dat[3:]:
                    fich.write(str(i)+" ")
                fich.close()
                await client.send_message(message.channel, "Réussi")
        elif message.content.startswith("!red testr"):
            dat = message.content.split(" ")
            if len(dat) != 3:
                await client.send_message(message.channel, "Erreur 4")
            elif exists(dat[2]):
                fich = open(dat[2],"r")
                texte = fich.read()
                fich.close()
                await client.send_message(message.channel, texte)
            else:
                await client.send_message(message.channel, "Erreur 5")
        elif message.content.startswith("!red testd"):
            dat = message.content.split(" ")
            if len(dat) != 3:
                await client.send_message(message.channel, "Erreur 6")
            elif exists(dat[2]):
                remove(dat[2])
                await client.send_message(message.channel, "Réussi")
            else:
                await client.send_message(message.channel, "Erreur 7")

client.run("NDM4MDQ4NTkzNzc4MzExMTY4.Db_I0w.2yvvfel6n860rxPA72HHYGvYUJo")