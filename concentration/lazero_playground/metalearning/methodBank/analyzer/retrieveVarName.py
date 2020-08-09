import inspect

y3=[0,1,2][2]
y2=y3
x,y,z = 1,y2,3

y0=2
y1=y
def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

print (retrieve_name(y))
