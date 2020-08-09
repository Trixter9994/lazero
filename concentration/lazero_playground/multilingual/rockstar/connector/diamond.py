import os
import re
import pandas as pd
# ALL YOUR BASE ARE BELONG TO US!
# WHO YOU ARE! NOT WHERE YOU CAME FROM!
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
def list_files(startpath):
# what does this fucking os.walk() return
    #superdictionary={}
    # at the beginning of the fucking thing we wanna to make things absolutely clear.
    maximum_depth=2
    depth_list=[]
    superlist=[2,[]]
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
        rhino=root.split("/")[1:]
#        rhino[0]=name_of_root
        crakn=[os.path.basename(root),0]+rhino[:-1]
        superlist.append(crakn)
        depth_list.append(len(crakn))
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
            grakn=[f,1]+rhino
            superlist.append(grakn)
            depth_list.append(len(grakn))
    superlist[0]=sorted(depth_list,reverse=True)[0]
    superlist[1]=depth_list
    return superlist
#            print("-----second mark-----")
            #print('{}{} {}'.format(subindent, f,level+1))

startpath="/data/data/com.termux/files/home/lazer/multilingual/rockstar/superdir"

# when run without the trailing slash, the root directory name will simply be printed out.
# we should make a comparation here.
# i think the former is better because it has the indentation preserved.

# startpath0="/data/data/com.termux/files/home/lazer/multilingual/rockstar/superdir/"
# Keep It Simple Stupid.
# Never Overestimate the Understanding Ability of Computer.
# Never Ever Think that Computer May Get Tired of Repetitive Tasks.
# this time we have integrated the fucking slash here.

omega=list_files(startpath)

#print(omega)

#sadist=[]
#masochist=[]

alpha=omega[0]
#print(alpha)
gamma=omega[1]
#print(gamma)
# things are now getting funny.
# i wrote shits.
# my code sucks, and it is fucking perfect.
delta=set(gamma)
#print(delta)
#for m in range(alpha):
#    masochist.append([""]*(len(omega)-2))
ultidick={}
for k in delta:
    ultidick[k]=[]
for r in range(len(omega)-2):
    beta=omega[r+2]
    ultidick[len(beta)].append(beta)
print(ultidick)
    # you get the list here.
#    sigma=alpha-gamma[r]
#    if sigma!=0:
#        for d in range(sigma):
#            beta+=[""]
#    sadist.append(beta)
for k in delta:
    sick={}
    sadist=ultidick[k]
#    print(sadist)
    masochist=[]
    for m in range(k):
        masochist.append([""]*len(sadist))
    for l in range(len(sadist)):
        for j in range(k):
            masochist[j][l]=sadist[l][j]
#    finaldick={}
    
#    for k in range(len(sadist)):
#        masochist[l][k]=sadist[k][l]
    for l in range(k):
        sick["{}{}".format("key",l)]=masochist[l]
#print (sick)
#numeric value preserved. don't even look.
    df = pd.DataFrame(sick)
# pandas is way fucking slow.
# keep it as a fucking habit?
# any alternatives?
    the_real_shit=df.to_csv(index=False)
#    print(the_real_shit)
    fuckyou=open("{}{}{}".format("gotcha",k-2,".csv"),"w+")
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
