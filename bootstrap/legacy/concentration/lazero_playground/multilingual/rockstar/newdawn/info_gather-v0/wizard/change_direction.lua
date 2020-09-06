fileFuck=io.open("core.log","r")
-- YOU ARE DEAD
nothingLeft=io.open("uponUs.log","w")
handle=io.popen("ls "..fileFuck:read())
fate=handle:read("*a")
nothingLeft:write(fate)
fileFuck:close()
nothingLeft:close()
