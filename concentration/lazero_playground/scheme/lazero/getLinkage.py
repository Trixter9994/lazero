# TODO: implement raw things and arbitrary tests.
import re
import random

def around(a, b):
  build = r'[^{}]+{}[^{}]+'.format(
      *[re.escape(b) for x in range(3)])
  return re.findall(build,a)

def reinforce(a,max_temp_length):
# TODO: levels in the chain.
    mtl=max_temp_length
    assert mtl>3 and type(mtl)==int
    level=0
    table=[]
    cand=0
    func=lambda y,z:{x:z[x][y] if len(z[x])>y else None for x in range(len(z))}
    for x in a:
        test=func(level,table)
        test0=[y for y in test.keys() if test[y]==x]
        if table==[]:
            table.append(x)
        elif test0!=[]:
            cand=random.choice(test0)
            #table[tx]+=x
        else:
            if level<max_temp_length:
                table[cand]+=x
            else:
                table.append(x)
                level=-1
        level+=1
    return table
