import discord
import os


async def changeroles(message, arguments):
    guild = message.guild
    current_role_str = arguments[0]
    new_role_str = arguments[1]
    roles_list = message.guild.roles
    create = True
    current_role = None
    new_role = None
    
    for i in roles_list:
        if current_role_str == i.name:
            current_role = i
        elif new_role_str == i.name:
            create = False
            new_role = i
            await message.channel.send('new role already exists adding them to users.')

    if create:
        new_role = await guild.create_role(name=new_role_str)
    
    
    if current_role == None:
        await message.channel.send('current role not found')
        return
    members = current_role.members
    for i in members:
        await i.add_roles(new_role)
    
    await message.channel.send('new role added, previous role can be removed')
    
    