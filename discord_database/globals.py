import json
class globals():
    def __init__(self , filename):
        self.type='discord_db.globals'
        self.filename=filename
        try:
            with open(filename+'.discord_db')as f:
                db=json.load(f)    
            db["global"]
        except:
            with open(filename+'.discord_db', 'w')as f:
                f.write('{"global":{}}')
        self.filename=filename
    def new(self,ctx):
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
            db['global'] [str(ctx.author.id)]={}
        with open(self.filename+'.discord_db', 'w')as f:
            json.dump(db,f)
        return db['global'][str(ctx.author.id)]

    def save(self,ctx,key,item):
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        
        db['global'][str(ctx.author.id)][key]=item
        with open(self.filename+'.discord_db','w')as f:
            json.dump(db,f)
        return db['global'][str(ctx.author.id)][key]
    def load(self,ctx,key):
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        return db['global'] [str(ctx.author.id)][key]

    def plus(self,ctx,key,item:float):
        if not isinstance(item, float) and not isinstance(item, int):
            yield TypeError('The "plus" only can use the "int" or "float" types!')
            return
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        db['global'] [str(ctx.author.id)][key]+=item
        with open(self.filename+'.discord_db', 'w')as f:
            json.dump(db,f)
        return db['global'] [str(ctx.author.id)][key]
