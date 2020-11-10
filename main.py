import os
import discord
import requests
from threading import Thread

# Change values below
serverId = # Example: 123456789123456789
botToken = # Example: "L1ZszTkJX77WicKA27xNpooTSWqqov8y86rNbDkA"
fileDirectory = # Example: "/home/user/Documents/", make sure to include a trailing slash

client = discord.Client()

def download(fileUrl, filename, channel):
	print("Downloading file: " + fileUrl)
	fileDownload = requests.get(fileUrl)
	if not os.path.exists(fileDirectory + str(channel)):
		os.makedirs(fileDirectory + str(channel))
	with open(fileDirectory + str(channel) + '/' + filename, 'wb') as file:
		file.write(fileDownload.content)

@client.event
async def on_message(message: str):
	if message.attachments and message.guild.id == serverId:
		for file in message.attachments:
			Thread(target=download, args=(''.join(file.url), file.filename, message.channel)).start()

client.run(botToken)
