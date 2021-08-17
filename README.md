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
# if you went to change to use global , change locals to globals like this:
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
    print('------------------------------------------')
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
### web server need  [pywebio](https://pypi.org/project/pywebio/) , it can auto install
## Changelogs:
#### 1.0.2
#### fix something(power by [AstroOrbis](https://github.com/AstroOrbis)) , web UI
#### 1.0.1
#### fix load

#### 1.0.0
#### first version
