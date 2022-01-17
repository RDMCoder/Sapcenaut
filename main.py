import discord
import os
import json
from discord.ext import commands
from discord.ext import commands, tasks
from itertools import cycle
import datetime
import asyncio
import random
import json
from keep_alive import keep_alive




def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]  

client = commands.Bot(command_prefix = get_prefix)
client.remove_command("help")

@client.event
async def on_guild_join(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)] = '/'

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes.pop(str(guild.id))

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

@client.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')





@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  await ctx.send("This extension has been loaded successfully!")


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  await ctx.send("This extension has been successfully unloaded!")

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')
  await ctx.send("The selected extension has been reloaded.")



@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} servers | /help"))
  print("Spacenaut just conquered Mars!")


@client.command()
async def ping(ctx):
  await ctx.send(f'Bzzz... bzzzz. Your transmission has been recieved. {round(client.latency * 1000)}ms')



@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "Help", description = "Use /help <command> for extended information on a command.",color = ctx.author.color)

  em.add_field(name = "Moderation", value = "Warn, Kick, Ban, Unban, Clear, Mute, Unmute,     Whois")
  em.add_field(name = "Fun", value = "Hello, Door, Ping, Rocket, Rickroll")

  await ctx.send(embed = em)


  @help.command()
  async def Kick(ctx):
    em = discord.Embed(title = "Kick", description = "Kicks a member from the guild.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/kick <member> [reason]")
    await ctx.send(embed = em)




  @help.command()
  async def Ban(ctx):
    em = discord.Embed(title = "Ban", description = "Bans a member from the guild.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/ban <member> [reason]")
    await ctx.send(embed = em)



  @help.command()
  async def Unban(ctx):
    em = discord.Embed(title = "Unban", description = "Unbans a member from the guild.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/unban <member>")
    await ctx.send(embed = em)



  @help.command()
  async def Clear(ctx):
    em = discord.Embed(title = "Clear", description = "Clears automatically 2 messages.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/clear [number of messages]")
    await ctx.send(embed = em)



  @help.command()
  async def Mute(ctx):
    em = discord.Embed(title = "Mute", description = "Mutes a member of the guild.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/mute <member>")
    await ctx.send(embed = em)



  @help.command()
  async def Unmute(ctx):
    em = discord.Embed(title = "Unmute", description = "Unmutes a member of the guild.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/unmute <member>")
    await ctx.send(embed = em)



  @help.command()
  async def Whois(ctx):
    em = discord.Embed(title = "Who is", description = "Tells information about a member of the guild.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/whois <member>")
    await ctx.send(embed = em)




  @help.command()
  async def Hello(ctx):
    em = discord.Embed(title = "Hello", description = "Says hi.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/hello")
    await ctx.send(embed = em)





  @help.command()
  async def Door(ctx):
    em = discord.Embed(title = "Door slam", description = "Slams a door.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/door")
    await ctx.send(embed = em)



  @help.command()
  async def Warn(ctx):
    em = discord.Embed(title = "Warn (not working)", description = "Warns a member of the guild.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/warn <member> [reason]")
    await ctx.send(embed = em)



  @help.command()
  async def Ping(ctx):
    em = discord.Embed(title = "Ping", description = "Sends a ping to the bot and shows the response time.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/ping")
    await ctx.send(embed = em)



  @help.command()
  async def Rocket(ctx):
    em = discord.Embed(title = "Rocket", description = "Launches a rocket into the space.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/rocket")
    await ctx.send(embed = em)




  @help.command()
  async def Rickroll(ctx):
    em = discord.Embed(title = "Rickroll", description = "Rickrools the mentioned member.",color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "/rickroll")
    await ctx.send(embed = em)





@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):

    await ctx.send("You can't do that.")
    await ctx.message.delete()

  elif isinstance(error, commands.MissingRequiredArgument):

    await ctx.send("Please enter all the required arguments. If you want more information, do '/help'.")
    await ctx.message.delete()

  else:

    raise error



@client.event
async def on_command_error(ctx, error): 
  if isinstance(error, commands.CommandNotFound): 
    em=discord.Embed(title=":x: Command not found.", description="Double-check if the command is correct.", color=0xff0000)
    await ctx.send(embed=em)
    await ctx.message.delete()







keep_alive() 
client.run(os.getenv('TOKEN'))