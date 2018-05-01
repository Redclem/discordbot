import discord
import asyncio
import random
from os.path import exists
from os import remove,mkdir,listdir

client = discord.Client()
version = "0.9"
dossier = "tests/"

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
        elif message.content.startswith("!red w"):
            dat = message.content.split(" ")
            if len(dat) < 4:
                await client.send_message(message.channel, "Erreur 3")
            else:
                fich = open(dossier+dat[2],"w")
                for i in dat[3:]:
                    fich.write(str(i)+" ")
                fich.close()
                await client.send_message(message.channel, "Réussi")
        elif message.content.startswith("!red r"):
            dat = message.content.split(" ")
            if len(dat) != 3:
                await client.send_message(message.channel, "Erreur 4")
            elif exists(dossier+dat[2]):
                fich = open(dossier+dat[2],"r")
                texte = fich.read()
                fich.close()
                await client.send_message(message.channel, texte.rstrip(" "))
            else:
                await client.send_message(message.channel, "Erreur 5")
        elif message.content.startswith("!red d"):
            dat = message.content.split(" ")
            if len(dat) != 3:
                await client.send_message(message.channel, "Erreur 6")
            elif exists(dossier+dat[2]):
                remove(dossier+dat[2])
                await client.send_message(message.channel, "Réussi")
            else:
                await client.send_message(message.channel, "Erreur 7")
        elif message.content.startswith("!red l"):
            for i in listdir(dossier):
                await client.send_message(message.channel, i)

if not exists(dossier):
    mkdir(dossier)

client.run("NDM4MDQ4NTkzNzc4MzExMTY4.DcpOJA.pXMbFiTkLNv79dmPIOCxSfyBA78")
