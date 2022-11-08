import spear
from spear.news import BBC_HOMEPAGE 
spear.init()
accum = True
bbc = BBC_HOMEPAGE()

bbc.pull()

bbc_all = bbc.all()

res = bbc.search('Congress')

print(res)




