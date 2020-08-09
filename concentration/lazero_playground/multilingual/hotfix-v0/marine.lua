superspliter = [[;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;]]
---------------------------------------------------
range = require("range_module.init")
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
	    if part ~="\n" and part ~="" then
        nb = nb + 1  
        result[nb] = part   
        lastPos = pos   
        if nb == maxNb then break end  
end
    end  
    
    -- Handle the last field   
    if nb ~= maxNb then  
        result[nb + 1] = string.sub(str, lastPos)   
    end  
--result[1]=nil
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
    for part, pos in string.gmatch(str, pat) do  if part~="\n" and part~="" then
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
--result[1]=nil
    return result   
end  

--command ="node duper-get.js java"

--the_fucking_url=[[http://www.baidu.com/link?url=nS2MGJqjJ4zBBpC8yDF8xDh8vibi1lVeE7gGr9UONBu]]
--fucking shit.
--[[command ="node supercat.js java 0"
handle = io.popen(command)
result = handle:read("*a")
handle:close()]]
command ="node supercat.js "..arg[1]       for iterable in range(2,#arg) do
command=command.." "..arg[iterable]
end
handle = io.popen(command)
result = handle:read("*a")
handle:close()
-- use local instead of using some functions.

supertable=Split(result,superspliter,nil)

one_fuck_all=""

-- never fucking use minus sign in variable name and fuck you!

for key,value in pairs(supertable) do
--	if key>1 then
--local	
supertable[key]=Splitv(value,"\n",2)
one_fuck_all=one_fuck_all.." "..supertable[key][2]
-- you little piece of shit!
-- forgot to add the mother fucking space!
-- the maximum item should be 2 thereafter.
-- fuckyou!
--[[	print (nextable[2])
	print (nextable[3])]]
	--[[for fuckingkey,fuckingvalue in pairs(nextable) do
		--if fuckingkey >1 then
		print("["..(fuckingkey-1).."]")
		-- YOU SET ME UP YOU PRICKS!
		-- the number 1 item is a fucking link.
		
		if fuckingkey==2 then
			-- fuck you asshole, you pricks.

		-- i always cheat myself.
	--	print(fuckingvalue)
	--else
		local command = "lua shell-args.lua "..fuckingvalue
		--let me see it first.
--		print(command)
		local handle=io.popen(command) 
		local result=handle:read("*a") 
		handle:close() 
--		print(result) 
		io.write(result)
		--the final return should be integrated.
	else
		print (fuckingvalue)
	end
		-- wtf is the difference between the fucking colon and the period?
		-- is this fucking usable?
		-- i just want the motherfucking real address!
		-- the fucking key ranges from 1 to 4, but we have removed the first one somehow.
		-- just define that shit in the original function.
		-- remove the motherfucking #1 item.
--	end
	end
--	print (value-processed)
	print ("--- this is the divide line ---")
end--]]
end
--end
--one_fuck_all_table={}

fuckyou_command = "lua shell-args.lua "..one_fuck_all
--print(one_fuck_all)
--i do not need that prick no more.
fuckyou_handle = io.popen(fuckyou_command)
fuckyou_result = Split(fuckyou_handle:read("*a"),"\n")
fuckyou_handle:close()
-- the table will be returned.
--result = Split(result0,"\n")
--[[print(fuckyou_result[1])
for dickkey,dickvalue in pairs(fuckyou_result) do
	supertable[dickkey][2]=dickvalue
end
]]

--i am gonna make it multithreaded.
--fucking shit. you bitchs are great.

for key,value in pairs(supertable) do
--	if key>1 then
--local	nextable=Splitv(value,"\n",2)
-- the maximum item should be 2 thereafter.
-- fuckyou!
--[[	print (nextable[2])
	print (nextable[3])]]
	for fuckingkey,fuckingvalue in pairs(supertable[key]) do
		--if fuckingkey >1 then
		print("["..(fuckingkey-1).."]")
		-- YOU SET ME UP YOU PRICKS!
		-- the number 1 item is a fucking link.
		
		if fuckingkey==2 then
			-- fuck you asshole, you pricks.

		-- i always cheat myself.
		print(fuckyou_result[key])

else
		--local command = "lua shell-args.lua "..fuckingvalue
		--let me see it first.
--		print(command)
--		local handle=io.popen(command) 
--		local result=handle:read("*a") 
--		handle:close() 
--		print(result) 
--		io.write(result)
		--the final return should be integrated.
--	else
		print (fuckingvalue)
		-- let's just test.
		-- if shits happen we change it later on.
end
		-- wtf is the difference between the fucking colon and the period?
		-- is this fucking usable?
		-- i just want the motherfucking real address!
		-- the fucking key ranges from 1 to 4, but we have removed the first one somehow.
		-- just define that shit in the original function.
		-- remove the motherfucking #1 item.
--	end
	end
--	print (value-processed)
	print ("--- this is the divide line ---")
end
--end

--this will automatically add the fucking return.
--another thread.
