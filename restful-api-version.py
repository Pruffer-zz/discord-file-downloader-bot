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
siteUrl = # Example: "https://example.com/", make sure to include a trailing slash
apiKey = # Example: "GyljUI0BnMo7ulS1EfNTzyQTGaJPxOjm"

client = discord.Client()

def download(fileUrl, filename, channel):
	print("Downloading file: " + fileUrl)
	path = fileDirectory + channel
	fileDownload = requests.get(fileUrl)
	files = {
		'file': fileDownload.content
	}
	data = {
		'json':("{"
			"\"location\":\"" + fileDirectory + "\","
			"\"filename\":\"" + filename + "\","
			"\"overwrite\":\"no\""
		"}")
	}
	headers = {
		"apikey": apiKey
	}
	print("Sending request for: " + filename)
	response = requests.post(siteUrl + "api.php/file/upload", files=files, data=data, headers=headers)
	print("Request finished for: " + filename)
	

@client.event
async def on_message(message):
	if message.attachments and message.guild.id == serverId:
		for file in message.attachments:
			Thread(target=download, args=(''.join(file.url), file.filename, str(message.channel))).start()

client.run(botToken)
