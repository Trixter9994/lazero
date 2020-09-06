superspliter = [[;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;]]
---------------------------------------------------
-- range = require("range_module.init")
-- fuckyeah!
-- you bitch!
function Split(str, delim, maxNb)   
    -- Eliminate bad cases...   
    if string.find(str, delim) == nil then  
        return { str }  
    end  
    if maxNb == nil or maxNb < 1 then  
        maxNb = 0    -- No limit   
    end  
    local result = {}  
    local pat = "(.-)" .. delim .. "()"   
    local nb = 0  
    local lastPos   
    for part, pos in string.gmatch(str, pat) do  
        nb = nb + 1  
        result[nb] = part   
        lastPos = pos   
        if nb == maxNb then break end  
    end  
    -- Handle the last field   
    if nb ~= maxNb then  
        result[nb + 1] = string.sub(str, lastPos)   
    end  
    return result   
end  

function Splitv(str, delim, maxNb)   
    -- Eliminate bad cases...   
    maxLimit=maxNb+1
    if string.find(str, delim) == nil then  
        return { str }  
    end  
    if maxNb == nil or maxNb < 1 then  
        maxNb = 0    -- No limit   
    end  
    local result = {}  
    local pat = "(.-)" .. delim .. "()"   
    local nb = 0
    local nb0 = 0
    local lastPos
    local lastPos0
    for part, pos in string.gmatch(str, pat) do  
--string.gfind() is renamed.
        nb0 = nb0 + 1 
	if nb0 <= maxLimit then
        result[nb0] = part
end
	lastPos0=pos
        if nb0 <= maxNb then 
		lastPos=lastPos0
		nb=nb0
	end
	
        if nb0 > maxLimit then result[maxLimit]=result[maxLimit]..delim..part end  
    end  
    -- Handle the last field   
    if nb ~= maxNb then 
-- this means not equal to the maxNb.
-- better make sure that is not real.
        result[nb + 1] = string.sub(str, lastPos)   
    end  
--[[local fuckingnumber=#result
    if fuckingnumber>maxLimit then
	    for i in range(maxLimit+1,fuckingnumber) do
		    result[i]=nil
	    end]]
    return result   
end  

--command ="node duper-get.js java"

--the_fucking_url=[[http://www.baidu.com/link?url=nS2MGJqjJ4zBBpC8yDF8xDh8vibi1lVeE7gGr9UONBu]]
--fucking shit.
command ="node super-duper.js java 0"
handle = io.popen(command)
result = handle:read("*a")
handle:close()
-- use local instead of using some functions.

supertable=Split(result,superspliter,nil)

for key,value in pairs(supertable) do
	if key>1 then
local	nextable=Splitv(value,"\n",3)
--[[	print (nextable[2])
	print (nextable[3])]]
	for fuckingkey,fuckingvalue in pairs(nextable) do
		if fuckingkey >1 then
		print("["..fuckingkey.."]")
		print(fuckingvalue)
	end
	end
--	print (value-processed)
	print ("--- this is the divide line ---")
end
end

--this will automatically add the fucking return.
--another thread.
