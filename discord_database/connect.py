from pip._internal import main as pip
try:
    import requests
    from requests.structures import CaseInsensitiveDict
except:
    pip.main(['install', 'requests'])
    import requests
    from requests.structures import CaseInsensitiveDict
from json import dumps


class connect():
    def __init__(self,url,username,password):
        self.url=url
        self.username=username
        self.password=password
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.username}:{self.password}"
        headers["Content-Type"] = "application/json"

    def load(self,ctx,key):
        data = dumps({"server":str(ctx.message.guild.id),"user":str(ctx.author.id),"key":key})
        resp = requests.post(f"{self.url}/load", headers=self.headers, data=data)
        return resp.json
    def save(self,ctx,key,item):
        data = dumps({"server":str(ctx.message.guild.id),"user":str(ctx.author.id),"key":key,'item':item})
        resp = requests.post(f"{self.url}/save", headers=self.headers, data=data)
        return resp.json
    def new(self,ctx,user):
        data=dumps({"server":str(ctx.message.guild.id),"user":str(ctx.author.id)})
        resp = requests.post(f"{self.url}/new", headers=self.headers, data=data)
        return resp.json

