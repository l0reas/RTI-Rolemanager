#modules
import discord
import Commands
import os
import json
import bot
import asyncio
from datetime import timedelta

class MyClient(discord.Client):
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #import the json files
        with open('config.json', encoding='utf-8') as config_file:
            config = json.loads(config_file.read())
        #definitions
        self.prefix = config.get('prefix')
        self.token = config.get('token')
        
            
    #async def on_ready(self):
        #channel = self.get_channel(self.channelId)
        #await channel.send("Hi there, I am RoleManager. My mainframe has been booted up!")

    async def run_command(self, message):
        cleanMessage = message.content.strip(self.prefix).lower()
        functionname = cleanMessage.split()[0]
        package = getattr(Commands, functionname)
        function = getattr(package, functionname)
        messageList = cleanMessage.split()
        argList = messageList[1:]
        await function(message, argList)
        return
    
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author == self.user:
            return
        
        if message.content.startswith(self.prefix):
            await self.run_command(message)
            return

        