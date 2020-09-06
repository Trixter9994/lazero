simple=[[hello you mot""""her fucker, you are now g""""oing to die.
you mother fucking whore!
fuck you dickh""""""ead!
all your""""" base are bel"""ong to us!]]
-- print(simple:gsub("\"","\\\""))
handle=io.popen("python sadomachist.py <<< \"\"\"\"\""..simple:gsub("\"","\\\"").."\"\"\"\"\"")
result=handle:read("*a")
handle:close()
print(result)
-- try to let other process take this shit down!
-- i suggest you to do this in two ways:
-- one is to save it to some file
-- two is use redis.
-- but you will not give this shit up, will you?
-- you will try to do this in stdin!
