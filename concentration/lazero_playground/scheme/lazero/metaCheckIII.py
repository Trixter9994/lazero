from jinja2 import Template
# result_buffer = []
import sys
cmdline=sys.argv[1].replace("-","_")
temp = """#import font_unicode
import {{ MODULE }}
from simpleStorageR import storeListV

strictness={{ STRICTNESS }}
stiffness="".join(["_" for x in range(strictness)])

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
        result = list(filter(lambda x: x[:strictness] != stiffness and x[-strictness:] !=
                             stiffness, list(filter(lambda x: len(x) > 4, dir(sub_package)))))
        result = list(
            map(lambda x: sub_package_name + "." + x, result))
        # print("\\n>>>SUB_PACKAGE<<<\\n",result)
        evaluation={}
        try:
            for x in result:
                try:
                    evaluation.update({x: eval(x) })
                except:
                    pass
        except:
            pass
    else:
        result = list(filter(lambda x: x[:strictness] != stiffness and x[-strictness:] !=
                             stiffness, list(filter(lambda x: len(x) > 4, dir(base_package)))))
        result = list(map(lambda x: base_package_name + "." + x, result))
        evaluation={}
        # this is dangerous. it is printable. not literal.
        try:
            for x in result:
                try:
                    evaluation.update({x: eval(x) })
                except:
                    pass
        except:
            pass
    return evaluation
    # l=list(map(lambda x:a.__name__+"."+x,dir(a)))


def recurCheck(main_module, max_depth, buff=[]):
    assert max_depth >= 0 and type(max_depth) == int
    if buff == []:
        c = checkSingle(main_module)
        # maybe it is because of the name.
        buff.append(c)
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
        return recurCheck(main_module, max_depth - 1, buff)
    else:
        return buff

if __name__ == "__main__":
# print(c)
    d = recurCheck({{ MODULE }}, {{ MAX_DEPTH }})
#print(d)
# do not print info for it.
    d=list(map(lambda x: {y:str(type(x[y])) for y in x.keys()}, d))
    # do not visualize the shit.
    # by the way , what the heck is the buffer?
    # print(d)
    # what the heck?
    # just check it.
    storeListV(d,"{{ MODULE }}")
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
"""
template = Template(temp) # strange.
result = template.render(MODULE=cmdline, MAX_DEPTH=7, STRICTNESS=1)
print(result)