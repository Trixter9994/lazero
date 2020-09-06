-- we plan to do this at once.
the_fucking_url=arg
--{[[http://www.baidu.com/link?url=nS2MGJqjJ4zBBpC8yDF8xDh8vibi1lVeE7gGr9UONBu]],[[http://www.baidu.com/link?url=mQRln1LKWUncYQMSCUu01Uq09GtFVObdNqylQdFpk3ebBca2mr5AzXeNyG31ljYB3dW5Ke9vJ2nPVEZ08vicwxSK0mVBg5KQWHUMXdqZcs3]]}
--this is the mother fucking table.
--fucking shit.
--easy you piece of shit.
handle={}
for key,value in ipairs(the_fucking_url) do
command ="curl -b baidu.cookies \""..value.."\" 2> /dev/null "
--psudocode above.
handle[#handle+1]= io.popen(command)
--is it threaded?
end

-- this shit is only used as two
-- you could increase it as you wish.

for key,value in pairs(handle) do
result = handle[key]:read("*a")
handle[key]:close()
-- use local instead of using some functions.
print (result)
end

