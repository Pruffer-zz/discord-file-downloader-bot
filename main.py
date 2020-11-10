import os
import discord
import requests
import random
import string
from threading import Thread

# Change values below
serverId = # Example: 123456789123456789
botToken = # Example: "L1ZszTkJX77WicKA27xNpooTSWqqov8y86rNbDkA"
fileDirectory = # Example: "/home/user/Documents/", make sure to include a trailing slash

client = discord.Client()

def renameFile(path, filename):
	characterCount = random.randint(1,15)
	changedFilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=characterCount)) + '-' + filename
	return changedFilename

def download(fileUrl, filename, channel):
	print("Downloading file: " + fileUrl)
	path = fileDirectory + channel
	fileDownload = requests.get(fileUrl)
	if not os.path.exists(path):
		os.makedirs(path)
	while os.path.isfile(path + '/' + filename):
		filename = renameFile(path, filename)
	with open(path + '/' + filename, 'wb') as file:
		file.write(fileDownload.content)

@client.event
async def on_message(message):
	if message.attachments and message.guild.id == serverId:
		for file in message.attachments:
			Thread(target=download, args=(''.join(file.url), file.filename, str(message.channel))).start()

client.run(botToken)
