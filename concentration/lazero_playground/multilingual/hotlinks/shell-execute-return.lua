command ="ls"
handle = io.popen(command)
result = handle:read("*a")
handle:close()
-- use local instead of using some functions.
print (result)
