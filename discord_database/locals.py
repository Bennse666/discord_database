import json
class locals():
    def __init__(self , filename):
        self.type='discord_db.locals'
        self.filename=filename
        try:
            with open(filename+'.discord_db')as f:
                db=json.load(f)    
            db["local"]
        except:
            with open(filename+'.discord_db', 'w')as f:
                f.write('{"local":{}}')
        self.filename=filename
    def new(self,ctx):
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        try:
            db['local'][str(ctx.message.guild.id)][str(ctx.author.id)]={}
        except KeyError:
            db['local'][str(ctx.message.guild.id)]={}
            db['local'][str(ctx.message.guild.id)][str(ctx.author.id)]={}
        except Exception as error:
            yield error
        with open(self.filename+'.discord_db', 'w')as f:
            json.dump(db,f)
        return db['local'][str(ctx.message.guild.id)][str(ctx.author.id)]

    def save(self,ctx,key,item):
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        
        db['local'][str(ctx.message.guild.id)][str(ctx.author.id)][key]=item
        with open(self.filename+'.discord_db','w')as f:
            json.dump(db,f)
        return db['local'][str(ctx.message.guild.id)][str(ctx.author.id)][key]
    def load(self,ctx,key):
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        return db['local'][str(ctx.message.guild.id)][str(ctx.author.id)][key]

    def plus(self,ctx,key,item:float):
        if not isinstance(item, float) and not isinstance(item, int):
            yield TypeError('plus only can use int or float')
            return
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        db['local'][str(ctx.message.guild.id)][str(ctx.author.id)][key]+=item
        with open(self.filename+'.discord_db', 'w')as f:
            json.dump(db,f)
        return db['local'][str(ctx.message.guild.id)][str(ctx.author.id)][key]
