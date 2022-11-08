import spear
from spear.news import BBC_HOMEPAGE as bbc
spear.init()
accum = True

bbc.pull()

bbc_all = bbc.all()

res = bbc.search('Israel')

print(res)




