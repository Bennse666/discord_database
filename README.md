## A database manager for Discord!

![discord_database_icon]https://github.com/cutebear0123/cutebear0123/blob/main/databasedatabase.png?raw=true()

### Example:
```python
from discord_database import locals
# connect to database
db=locals('test')
# create a bot
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('------------------------------------------')
@bot.command()
async def new(ctx):
    #Adds a new user
    await ctx.send(db.new(ctx))
@bot.command()
async def save(ctx,key,item):
    #Creates ("saves") a new item
    await ctx.send(db.save(ctx,key,item))
@bot.command()
async def load(ctx,key):
    #Loads an item
    await ctx.send(db.load(ctx,key))
```
# If you want to use globals instead of locals, switch them around accordingly:
```python
from discord_database import globals
# Conncets to the database
db=globals('test')

# Declares the bot
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('------------------------------------------')
@bot.command()
async def new(ctx):
    #Adds a new user
    await ctx.send(db.new(ctx))
@bot.command()
async def save(ctx,key,item):
    #Saves (creates) a new item
    await ctx.send(db.save(ctx,key,item))
@bot.command()
async def load(ctx,key):
    #Loads an item
    await ctx.send(db.load(ctx,key))
```
## web UI
```python
import discord_database
from discord_database import web
db=discord_database.locals('test')
webs=web.locals('test')
webs.run()

#or
import discord_database
from discord_database import web
db=discord_database.globals('test')
webs=web.globals('test')
webs.run()
```
# share database
```python
# import
import discord_database
from discord_database import share
# connect to database
db=discord_database.locals('test')
# share database
shares=share.local
# set share filename
shares.filename="test"
# create a user access: 1=read,2=write,3=create user
shares.add_user('username','password',2)
# create server in port 8888
shares.run()
# or
# import
import discord_database
from discord_database import share
# connect to database
db=discord_database.globals('test')
# share database
shares=share.globals
# set share filename
shares.filename="test"
# create a user access: 1=read,2=write,3=create user
shares.add_user('username','password',2)
# create server in port 8888
shares.run()
```
# connect to database server
```python

# import
import discord_database
from discord_database import connect
# create a bot
import discord
from discord.ext import commands

# connect to database server
c=connect.connect('http://your_server_ip:8888',username,password)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('------------------------------------------')
@bot.command()
async def load(ctx,key):
    # Loads an item
    await ctx.send(c.load(ctx,key))
@bot.command()
async def save(ctx,key,item):
    # Saves (creates) a new item
    await ctx.send(c.load(ctx,key,item))
@bot.command()
async def new(ctx):
    # create a new user
    c.new(ctx)


```
## Changelogs:
#### 1.0.3
#### share database
#### 1.0.2
#### fix something(power by [AstroOrbis](https://github.com/AstroOrbis)) , web UI
#### 1.0.1
#### Fix the "load" command

#### 1.0.0
#### Initial release
