Table={
	[1]={"pdf","document","doc",""},
	[2]={"reader","conver","format",""},
	[3]={"txt","text","word",""}
}
--shorter, and more common is better.
--not even the whole word.
Table0={}
spliter="---------fuckyou---------"
function map_all (fcn, tab, idx, ...)
    if idx < 1 then
	    --count of the list.
	--print("--spliter--")
	-- this is the print-them-all function.
        fcn(...)
	--print("--spliter--")
	-- it is appending the thing on the back of argument list.
    else
        local t = tab[idx]
	-- length minus one.
        for i = 1, #t do
		--print("--spliter0--")
		map_all(fcn, tab, idx-1, t[i], ...) 
		--print("--spliter0--")
	end
    end
end

function appendnow(...)
	local shit=""
	for fuck,nothing in ipairs({...}) do
		if nothing~=""  then
			shit=shit.." \""..nothing.."\""
		end
	end
	if shit~="" then
		Table0[#Table0+1]=shit
	end
end

map_all(appendnow, Table, #Table)

--[[for x ,v in ipairs(Table0) do
	print(v)
end]]

handle={}                                  for key,value in ipairs(Table0) do
	command ="apt-cache search"..value  
	-- no trailing space.
--psudocode above.     
	handle[#handle+1]= io.popen(command)       --is it threaded?                  
end   

for key,value in pairs(handle) do

	result = handle[key]:read("*a")
	handle[key]:close()                        -- use local instead of using some functions.
--	print (result)
	print(Table0[key])
	print(spliter)
	io.write(result)
	print(spliter)
end

--anything is global here.
-- what is this shit all about?
--does that mean we have to append this fuck to a candidate list?
