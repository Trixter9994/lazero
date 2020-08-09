#import font_unicode
import scipy
import time as time_notsame_absolute
from simpleStorageR import storeListV


strictness=2
stiffness="".join(["_" for x in range(strictness)])

def binary_scan(a):
    if len(a)>strictness*2:
        if a[:strictness]==stiffness and a[-strictness:]==stiffness:
            return True
    return False

def chainScan(a):
    return [binary_scan(x) for x in a]

def filter_scan(a):
    f=chainScan(a)
    f0=list(map(int,f))
    gf=4
    if len(f0)>gf:
        fg=sum(f0[gf:])
        if fg:
            return False
    f0=sum(f0)
    if f0>=2:
        return False
    y=0
    for x in f:
        if x:
            y+=1
            if y>=2:
                return False
                # break
                # i didn't wrote this.
        else:
            y=0
    return True


def filter_out(a):
    return list(filter(lambda x: filter_scan(x) and len(x) == len(set(x)), a))

def b_global(y):
    return list(filter(lambda x: len(x) > 0, y.split(".")))


def checkSingle(base_package, sub_package=None, sub_package_name=None):
    base_package_name = base_package.__name__
    # exec("{} = base_package".format(base_package_name))
    # TODO: create standalone templates.
    # TODO: get specs from stringified modules.
    # TODO: migrating to automatic document generator.
    # TODO: allowing prebuild modules
    # TODO: real-time decision making to reduce calculation
    # TODO: restriction based on data size
    # TODO: scanning loosely arranged codebase (not a module)
    # TODO: self-propelling learning
    # locals.update(global_parameters)
    if sub_package is not None:
        result = dir(sub_package)
        result = list(
            map(lambda x: b_global(sub_package_name) + [x], result))
        result = filter_out(result)
        result = list(map(lambda x: ".".join(x), result))
        evaluation = {}
        try:
            for x in result:
                try:
                    evaluation.update({x: eval(x)})
                except:
                    pass
        except:
            pass
    else:
        result = dir(base_package)
        # result = list(filter(lambda x: x[:strictness] != stiffness and x[-strictness:] !=
        #                      stiffness, list(filter(lambda x: len(x) > 4, dir(base_package)))))
        result = list(map(lambda x: [base_package_name, x], result))
        result = filter_out(result)
        result = list(map(lambda x: ".".join(x), result))
        evaluation = {}
        try:
            for x in result:
                try:
                    evaluation.update({x: eval(x)})
                except:
                    pass
        except:
            pass
    return evaluation

def recurCheck(main_module, max_depth, buff=[]):
    print("at level", max_depth)
    t=time_notsame_absolute.time()
    assert max_depth >= 0 and type(max_depth) == int
    if buff == []:
        c = checkSingle(main_module)
        # maybe it is because of the name.
        buff.append(c)
        print("time spent",time_notsame_absolute.time()-t)
        return recurCheck(main_module, max_depth - 1, buff)
    elif max_depth > 0 and buff[-1] != {}:
        d = {}
        # print(buffer)
        # for c in buffer[-1]:
        c = buff[-1]
        for e in c.keys():
            # merged result.
            d.update(checkSingle(main_module, c[e], e))
        buff.append(d)
        print("time spent",time_notsame_absolute.time()-t)
        return recurCheck(main_module, max_depth - 1, buff)
    else:
        return buff

if __name__ == "__main__":
# print(c)
    d = recurCheck(scipy, 5)
#print(d)
# suggest using other things?
# do not print info for it.
    d=list(map(lambda x: {y:str(type(x[y])) for y in x.keys()}, d))
    # do not visualize the shit.
    # by the way , what the heck is the buffer?
    # print(d)
    # what the heck?
    # just check it.
    storeListV(d,"scipy")
#    for x in d.keys():
#    print(str(d))
#        print(x)
#    print(d)
# result_buffer=d
# def combine(a,b):
#     a0=checkSingle(a,b)
#     a1=list(map(lambda x:".".join(a,x),a0))
#     return a1

# def typecheck(a,b):
#     d=type(eval(a) if type(a)== str else a)
#     return d

# def typeBatch(a,b):
#     d=combine(a,b)
#     d0=list(map(lambda x: (x,typecheck(x)),d))
#     return d0
