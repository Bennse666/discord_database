import json
def help():
    helps='''
    command:
    locals.new :new user,arguments:ctx
    globals.new :new user in all globsl,arguments:ctx
    locals.load:load user data,arguments:ctx,item
    globals.load:load user data in global,arguments:ctx,item
    locals.save:save user data,arguments:ctx,key,item
    globals.save:save user data in global,arguments:ctx,key,item
    locals.plus:plus a number to a key,argquments:ctx,key,item(float)
    globals.plus:plus a number to a key in global,argquments:ctx,key,item(float)
    '''
    print(helps)
    return helps
from .globals import globals
from .locals import locals