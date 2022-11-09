from spear.news import BBC_HOMEPAGE 

accum = True
bbc = BBC_HOMEPAGE()

bbc.pull()

bbc_all = bbc.all()

hits = bbc.search('USA')

print([hit.url for hit in hits])




