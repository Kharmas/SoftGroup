import  re

ex = 'fu, tofu, snafu'
ex1 = 'futz, fusillade, functional, discombobulated'

pat = re.compile(r'(\w*fu\b)')
res = pat.findall(ex)
res1 = pat.findall(ex1)
print(res,res1)