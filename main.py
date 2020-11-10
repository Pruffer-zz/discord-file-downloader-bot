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

def check_file(path, file):
	if os.path.isfile(path + '/' + file):
		characterCount = random.randint(1,15)
		changedFile = ''.join(random.choices(string.ascii_uppercase + string.digits, k=characterCount)) + '-' + file
		return changedFile
	else:
		return file

def download(fileUrl, filename, channel):
	print("Downloading file: " + fileUrl)
	path = fileDirectory + str(channel)
	fileDownload = requests.get(fileUrl)
	if not os.path.exists(path):
		os.makedirs(path)
	filename = check_file(path, filename)
	while os.path.isfile(path + '/' + filename):
		check_file(path,filename)
	with open(path + '/' + filename, 'wb') as file:
		file.write(fileDownload.content)

@client.event
async def on_message(message: str):
	if message.attachments and message.guild.id == serverId:
		for file in message.attachments:
			Thread(target=download, args=(''.join(file.url), file.filename, message.channel)).start()

client.run(botToken)
