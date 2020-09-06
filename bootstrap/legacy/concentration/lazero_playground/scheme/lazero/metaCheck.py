from jinja2 import Template
# result_buffer = []
temp = """import {{ MODULE }}

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
        # print(result)
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


def recurCheck(main_module, max_depth, buffer=[]):
    assert max_depth >= 0 and type(max_depth) == int
    if buffer == []:
        c = checkSingle(main_module)
        buffer.append(c)
        return recurCheck(main_module, max_depth - 1, buffer)
    elif max_depth > 0 and buffer[-1] != {}:
        d = {}
        # print(buffer)
        # for c in buffer[-1]:
        c = buffer[-1]
        for e in c.keys():
            d.update(checkSingle(main_module, c[e], e))
        buffer.append(d)
        return recurCheck(main_module, max_depth - 1, buffer)
    else:
        return buffer


# print(c)
d = recurCheck({{ MODULE }}, {{ MAX_DEPTH }})
print(d)
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
template = Template(temp)
result = template.render(MODULE='numpy', MAX_DEPTH=7, STRICTNESS=1)
print(result)
# exec(result)
# print(result_buffer)
