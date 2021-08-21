from pip._internal import main as pip
from .globals import globals
import json
try:
    from pywebio.session import run_js
    from pywebio import start_server
    from pywebio.output import put_table,toast
    from pywebio.input import input_group,NUMBER,input

except:
    pip.main(['install', 'pywebio'])
    from pywebio.session import run_js
    from pywebio import start_server
    from pywebio.output import put_table,toast
    from pywebio.input import input_group,NUMBER,input
class globals():
    def __init__(self,filename):
        self.filename=filename
    def main(self):
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        a=db['global']
        b=[['id','thing']]
        for i in a:
            b.append([i,a[i]])
        put_table(b)
        info = input_group("User info",[
            input('Input id', name='id', type=NUMBER),
            input('Input key', name='key'),
            input('Input item', name='item')
            ])
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        item=[]
        items=info["item"].split('/')
        if len(items)!=2:
            toast('error! it only support int,float,str,bool')
        else:
            if items[0]=='int':
                item=int(items[1])
            elif items[0]=='float':
                item=float(items[1])
            elif items[0]=='str':
                item=str(items[1])
            elif items[0]=='bool':
                item=bool(items[1])
            else:
                item=items[1]
            db['global'][str(info["id"])][info["key"]]=item
            with open(self.filename+'.discord_db','w')as f:
                json.dump(db,f)
        run_js("location.reload(true);")

    def run(self):
        start_server(self.main,port=8080,debug=True)
class locals():
    def __init__(self,filename):
        self.filename=filename
    def main(self):
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        a=db['local']
        b=[['server','id','thing']]
        for i in a:
            for ii in a[i]:
                b.append([i,ii,a[i][ii]])
        put_table(b)
        info = input_group("User info",[
            input('server id', name='server', type=NUMBER),
            input('user id', name='id', type=NUMBER),
            input('key', name='key'),
            input('item', name='item')
            ])
        with open(self.filename+'.discord_db')as f:
            db=json.load(f)
        item=[]
        items=info["item"].split('/')
        if len(items)!=2:
            toast('error! it only support int,float,str,bool')
        else:
            if items[0]=='int':
                item=int(items[1])
            elif items[0]=='float':
                item=float(items[1])
            elif items[0]=='str':
                item=str(items[1])
            elif items[0]=='bool':
                item=bool(items[1])
            else:
                item=items[1]
            db['local'][str(info["server"])][str(info["id"])][info["key"]]=item
            with open(self.filename+'.discord_db','w')as f:
                json.dump(db,f)
        run_js("location.reload(true);")

    def run(self,port=8080):
        start_server(self.main,port=port,debug=True)
