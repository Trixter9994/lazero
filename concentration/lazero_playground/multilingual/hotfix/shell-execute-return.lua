command ="node duper-get.js java"
handle = io.popen(command)
result = handle:read("*a")
handle:close()
-- use local instead of using some functions.
print (result)
