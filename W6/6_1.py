import  re

ex = 'afoot, catfoot, dogfoot, fanfoot, foody, foolery, foolish, foster, footage, foothot, footle,footpad, footway, hotfoot, jawfoot, mafoo, nonfood, padfoot, prefool, sfoot, unfool'
ex1 = 'Atlas, Aymoro, Iberic, Mahran, Ormazd, Silipan, altered, chandoo, crenel , crooked, fardo, folksy, forest, hebamic, idgah, manlike, marly, palazzo, sixfold, tarrock, unfold'

pat = re.compile(r'.*fo{2,2}\w*')
res = pat.findall(ex)
res1 = pat.findall(ex1)
print(res,res1)