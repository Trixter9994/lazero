import pandas as pd
from dosage import drug
verbose=[]
# add new layers. I write custom filters to do this job.
# get the wrapper of html file.
# get four distinct values:
# number word code
v=(lambda l:[item for sublist in l for item in sublist])
v0=(lambda x: x if type(x[0]).__name__ in ["int","str"] else v0(v(x)))
cleanUp=(lambda x,y:list(filter((lambda x:x not in [y,""]),x.split(y))))
reClean=(lambda x,y: v([cleanUp(x0,y) for x0 in x]))
with open("sample/evil.html") as fuck:
    verbose=reClean(cleanUp(fuck.read(),"\n")," ")
#verbatism=[verbose[-1]]+verbose[:-1]
# better return a list.
df=pd.DataFrame(drug(verbose))
with open("canonical1.csv","w+") as hentai:
    hentai.write(df.to_csv(index=False))
