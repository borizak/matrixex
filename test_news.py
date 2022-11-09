import spear
from spear.news import BBC_HOMEPAGE 

accum = True
bbc = BBC_HOMEPAGE()

bbc.pull()

bbc_all = bbc.all()

res = bbc.search('Bremen')

print(res)




