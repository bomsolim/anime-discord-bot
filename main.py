import discord
import os
import requests
import json

my_secret = os.environ['DISCORD_TOKEN']
client = discord.Client()

def get_anime():
  response = requests.get("https://api.jikan.moe/v4/random/anime")
  json_data = json.loads(response.text)
  title_anime = json_data['data']['title']
  img_anime = json_data['data']['images']['jpg']['image_url']
  return(title_anime, img_anime)


@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg.startswith('$anime'):
    anime = get_anime()
    await message.channel.send(anime)

client.run(my_secret)

