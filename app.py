import discord
from discord import app_commands
from discord import File
from discord.ext import commands
from PIL import ImageFont
from easy_pil import Editor,load_image_async,Font

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client( intents=discord.Intents.all() )

guild_id = 0

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")
	# await tree.sync( guild = discord.Object(id = guild_id ) )

#

tree = app_commands.CommandTree(client)

@tree.command( name = "test", description = "testing", guild = discord.Object(id = guild_id ))
async def self( interaction : discord.Interaction ):
	# print( interaction.user )
	await interaction.response.send_message(f"Hello {interaction.user.name}")

#

"""
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('ping'):
		await message.channel.send("pong", reference=message)
"""

# bot = commands.Bot( command_prefix='>', intents=discord.Intents.all() )

# @bot.event
@client.event
async def on_message(message): # on_member_join

	if message.author == client.user:
		return

	member = message.author

	font = ImageFont.truetype(font="Poppins-Bold.ttf", size=50)

	channel = member.guild.system_channel

	background = Editor("pic1.jpg")

	# try:
	profile_image = await load_image_async(member.avatar.url)
	# except:
		# pass

	profile = Editor(profile_image).resize( (150,150) ).circle_image()
	
	# poppins = Font.poppins(size=50,variant="bold")
	# poppins_small = Font.poppins(size=20,variant="light")

	background.paste( profile, (325,90) )
	background.ellipse( (325,90) , 150, 150, outline="white", stroke_width=5 )

	background.text( (400,260) , f"{member.name}", color="white", font=font, align="center" )

	# background.text( (400,260) , f"WELCOME TO {member.guild.name}", color="white",font="poppins",align="center" )
	# background.text( (400,325) , f"{member.name}#{member.discriminator}", color="white",font="poppins_small",align="center" )

	file = File( fp=background.image_bytes, filename="pic1.jpg")

	# await channel.send( f"Hello {member.name}! Welcome to {member.guild.name}" )
	await channel.send( file=file )

#

client.run("")
