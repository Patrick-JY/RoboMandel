import discord
from boto.s3.connection import S3Connection
client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    




@client.event
async def on_member_join(member):
    await member.send("Welcome to Inverse's discord server! Please Enter your World of Warcraft Character Name")



    def check(m):
        return m.author == member

    msg = await client.wait_for('message', check = check)

    await member.edit(nick = msg.content[:12])
    print(msg.content)
    await member.send("Thank you")
   

client.run(os.environ['SECRET_TOKEN'])
