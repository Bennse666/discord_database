## a database for discord \n
### example
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
    print('We have logged in as {0.user}'.format(bot))
    print('We have logged in as {0.user}'.format(bot))
@bot.command()
async def new(ctx):
    #add a new user
    await ctx.send(db.new(ctx))
@bot.command()
async def save(ctx,key,item):
    #save/create a item
    await ctx.send(db.save(ctx,key,item))
@bot.command()
async def load(ctx,key):
    #load item
    await ctx.send(db.load(ctx,key))
```
# if you went to change to use global , change locals to globals like this
```python
from discord_database import globals
# connect to database
db=globals('test')
# create a bot
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('We have logged in as {0.user}'.format(bot))
    print('We have logged in as {0.user}'.format(bot))
@bot.command()
async def new(ctx):
    #add a new user
    await ctx.send(db.new(ctx))
@bot.command()
async def save(ctx,key,item):
    #save/create a item
    await ctx.send(db.save(ctx,key,item))
@bot.command()
async def load(ctx,key):
    #load item
    await ctx.send(db.load(ctx,key))
```
## update
#### 1.0.1
#### fix load
#### 1.0.0
#### first version
'''
