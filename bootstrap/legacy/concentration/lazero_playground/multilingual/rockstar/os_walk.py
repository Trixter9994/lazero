import os
# we should make it simpler.
# unless  you wanna die.

# we should make things clearer.
# directory-like object must be stored as a dictionary object, while files are stored inside a list. 
# while you can achieve this by something called numric and alphabetical differenciation, or some special prefix, even some metatable constrains
def list_files(startpath):
# what does this fucking os.walk() return
    superdictionary={}
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        # all you've got is this fucking freaky levels.
        # do you really need this dictionary?
        # you wanna analyze it locally?
        # my instinct tells me that you shall never be doing this.
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        print("first mark")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print("second mark")
            print('{}{}'.format(subindent, f))

startpath="/data/data/com.termux/files/home/lazer/multilingual/rockstar/superdir"

# when run without the trailing slash, the root directory name will simply be printed out.
# we should make a comparation here.
# i think the former is better because it has the indentation preserved.

startpath0="/data/data/com.termux/files/home/lazer/multilingual/rockstar/superdir/"

# this time we have integrated the fucking slash here.

list_files(startpath)

print("\n----[the fucking divide line]----\n")

list_files(startpath0)

print("\n----[the fucking divide line]----\n")

print(os.walk(startpath))

print("\n----[the fucking divide line]----\n")

print(list(os.walk(startpath0)))
# this is really useless.
# i do not think this is necessary to print it out directly.
# need preprocessing.
