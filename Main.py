#modules
import discord
import MyClient
import Commands
import os
import bot
import asyncio
from datetime import timedelta

#Variables
if __name__ == "__main__":
    #setup

    client = MyClient.MyClient()
    client.run(client.token)