## A database manager for Discord!
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
## Changelogs:

#### 1.0.1
#### Fix the "load" command

#### 1.0.0
#### Initial release
