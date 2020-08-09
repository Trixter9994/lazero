import os, re, sqlite3
import pandas as pd
#import sqlite3
# remember that we need to merge relative path to absolute path once we find it.
# you could keep something like UUID here.

def superskimmer(path):
    path0=list(filter((lambda x:x!=""),path.split("/")))[:-1]  
    p0="" 
    for p in path0: 
        p0+=("/"+p) 
    return p0
# anything called DROP DATABASE here?
# ALL YOUR BASE ARE BELONG TO US!
# WHO YOU ARE! NOT WHERE YOU CAME FROM!
# I DON'T GIVE A FUCK WHO YOU ARE!
# hey! generate some fucking csv file!
# and then load it with the fucking mechanism.
# i want to know about it.
# the structure could be rather simple.
# each line starts with the fucking directory name.
# and then the following subdirectory or other shits.
# or simply doing this, make a simple distinction over shits.
# store the fucking category along with the fucking shit.
# we would make it even.
# when the number is 0, it means directory.
# when it is 1, it is a fucking file!
# but how do we escape the fucking shit?
# i mean if we use the delimiter as content inside the csv file!
# we should make it simpler.
# unless  you wanna die.
# export it using profressional tools.
# we should make things clearer
##################################################################################
#                                                                                #
# EACH LINE IS SIMPLY A ONE_LINER REPRESENTING ONE SINGLE DIRETORY_FILE HIERACHY #
#                                                                                #
##################################################################################
# which make things much simpler.
# you could use pandas to make this happen.
# remember that it could be trinary or binary here.
# if you want binary, then you should export two files.
# if you want trinary, then you should export only one single file but with an extra column.
# anyway, you decice which one to be stored.
# directory-like object must be stored as a dictionary object, while files are stored inside a list. 
# while you can achieve this by something called numric and alphabetical differenciation, or some special prefix, even some metatable constrains
"""
def list_files(startpath):
# what does this fucking os.walk() return
    #superdictionary={}
    # at the beginning of the fucking thing we wanna to make things absolutely clear.
#    maximum_depth=2
#    depth_list=[]
    superlist=[]
    name_of_root=os.path.basename(startpath)
    # this is the list that we are gonna to return.
    # to change this into some fucking csv file is as easy as shit.
    for root, dirs, files in os.walk(startpath):
        #level = root.replace(startpath, '').count(os.sep)
        # all you've got is this fucking freaky levels.
        # do you really need this dictionary?
        # you wanna analyze it locally?
        # my instinct tells me that you shall never be doing this.
        #indent = ' ' * 4 * (level)
#       print(level)
#        print("-----first mark-----")
        #print(os.path.basename(root))
        #print(root)
        # it seems to be a string.
        # oh never forget the locate database.
        # the base is presumed.
        # if you want to expand the filesystem tree, remember to do something called the root-finding.
        # you need to make sure which level is the first common place for all.
        # usually this can be done by checking the pwd link.
        # and it is fucking damn easy.
        # but what should be done after this?
        # how could you do this then?
        # i suggest you to use the full fucing path.
        # though it will be tedious, you can always get the joy out of shit.
        # and it could be reusable.
        # never fucking mind.
        # i can drop database every fucking day.
        # i will deal with it later on.
        # the first priority is this fucking unicode standard.
        rhino=re.sub(startpath,"",root).split("/")
        rhino[0]=name_of_root
        crakn=[os.path.basename(root),0,len(rhino[:-1])]
        try:
            crakn.append(rhino[:-1][-1])
        except:
#            pass
# this is the root dir.
            crakn.append("")
        superlist.append(crakn)
#        depth_list.append(len(crakn)-1)
        # you can decide the comma values by the maximum depth.
        # to make it way simpler than anything, we append the directory after the type identifier..
        #print("0")
        # first we make sure our base directory is connected.
        # next we make the files under it get connected.
        #print('{}{}/ {}'.format(indent, os.path.basename(root),level+1))
#        print("-----first mark-----")
        #subindent = ' ' * 4 * (level + 1)
        for f in files:
#            print("-----second mark-----")
            grakn=[f,1,len(rhino),rhino[-1]]
            superlist.append(grakn)
#            depth_list.append(len(grakn))
#    superlist[0]=sorted(depth_list,reverse=True)[0]
#    superlist[1]=depth_list
    return superlist
"""
#            print("-----second mark-----")
            #print('{}{} {}'.format(subindent, f,level+1))

#startpath="/data/data/com.termux/files/home/lazer/multilingual/rockstar/superdir"
startpath="/data/data/com.termux/files/home/lazer/multilingual/rockstar/unicode-table-data"

# when run without the trailing slash, the root directory name will simply be printed out.
# we should make a comparation here.
# i think the former is better because it has the indentation preserved.

# startpath0="/data/data/com.termux/files/home/lazer/multilingual/rockstar/superdir/"
# Keep It Simple Stupid.
# Never Overestimate the Understanding Ability of Computer.
# Never Ever Think that Computer May Get Tired of Repetitive Tasks.
# this time we have integrated the fucking slash here.
"""
omega=list_files(startpath)

#print(omega)
for nintendo in range(len(omega)):
    omega[nintendo].insert(0,nintendo)
"""
sadist=[[],[],[],[]]
"""
masochist=[]
"""
conn = sqlite3.connect('tits.db')
cursor = conn.execute("SELECT id, name, type,depth,parent ,miscellaneous FROM subdir ORDER BY depth")
terminator=[]
# the id starts from zero.
for list0 in cursor:
    sugar=list(list0[:3])
    newbie=list0[4]
    honker=list0[3]
    dreado=list0[5]
    if newbie!=None:
        cur=conn.execute("SELECT id,name,miscellaneous FROM subdir WHERE name='{}' AND depth={};".format(newbie,honker-1))
        for shit in cur:
            if shit[2]==superskimmer(dreado):
                terminator.append(sugar+[shit[0]])
            else:
                pass
    else:
        terminator.append(sugar+[None])

#print(terminator)

# the terminator is ready here.

# it is great.
# but we need to connvert this into csv file.
# the number is 4 here.

#sql = ("CREATE INDEX index0 ON subdir (name);")
# sql0 = ("CREATE INDEX index1 ON subdir (id);")

#sql1 = ("CREATE INDEX index2 ON subdir (depth);")
#conn.execute(sql)
#conn.execute(sql1)
 # you shall not execute it every time.
"""conn.execute('''CREATE TABLE subdir
 (id INT PRIMARY KEY     NOT NULL,
name           TEXT    NOT NULL,
 type         TINYINT     NOT NULL,
 depth TINYINT NOT NULL,
parent TEXT );''')"""
"""
for a,b,c,d,e in omega:
    if e!="":
        conn.execute("INSERT INTO subdir (id,name,type,depth,parent)  VALUES ( {},'{}',{},{},'{}');".format(a,b,c,d,e))
    else:
        conn.execute("INSERT INTO subdir (id,name,type,depth)  VALUES ( {},'{}',{},{});".format(a,b,c,d))
"""
# do not scan the one with depth 0.

#conn.commit()
conn.close()

"""
alpha=omega[0]
print(alpha)
gamma=omega[1]
print(gamma)"""
# things are now getting funny.
# i wrote shits.
# my code sucks, and it is fucking perfect.
#
#for m in range(alpha):
#    masochist.append([""]*(len(omega)-2))

#for r in range(len(omega)-2):
#    beta=omega[r+2]
#    sigma=len(beta)
#    if sigma!=0:
#        for d in range(sigma):
#            beta+=[""]
#    sadist.append(beta)

sick={}

#print(terminator)

for l in range(4):
    sadist[l]+=[""]*len(terminator)
#for l in range(4):
    for k in range(len(terminator)):
        sadist[l][k]=terminator[k][l]
    sick["{}{}".format("key",l)]=sadist[l]

#print (sick)
#numeric value preserved. don't even look.
df = pd.DataFrame(sick)
# an equivalent approach will be depth + parentname.
# pandas is way too fucking slow.
# keep it as a fucking habit?
# any alternatives?
the_real_shit=df.to_csv(index=False)
#print(the_real_shit)
fuckyou=open("gotcha.csv","w+")
fuckyou.write(the_real_shit)
fuckyou.close()
    # you wanna to do this in pandas?
    # better convert this!
# print("\n----[the fucking divide line]----\n")

# list_files(startpath0)

#print("\n----[the fucking divide line]----\n")

# make index on those that change the most.
#print(os.walk(startpath))

#print("\n----[the fucking divide line]----\n")

# print(list(os.walk(startpath)))
# maybe the representation sucks so i cannot take care of simplification and efficiency at the same time.
# if exists, my machine will integrate it.
# you could integrate the root directory finding process into the cypher text.
# tuples inside.
# this is really useless.
# i do not think this is necessary to print it out directly.
# need preprocessing.
# always remember that the name of our very fucking phone is of the root directory.
# I need interactions between search engines.