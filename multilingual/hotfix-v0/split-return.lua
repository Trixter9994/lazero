--;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

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
--string.gfind() is renamed.
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

fuck="shit\nfuck\nshitfuck\nall your base are belong to us"

fuckall=Split(fuck,"\n",2)
asshole=Split(fuck,"\n",1)
bitchass=Split(fuck,"\n",3)

function shitshow(dicktable)
	for vagina,pussy in ipairs(dicktable) do
		print(vagina.." --fuckyou-- "..pussy)
	end
end

print("+1 fuckall")
shitshow(fuckall)
print("+2 fuckall")
shitshow(asshole)
print("+3 fuckall")
shitshow(bitchass)
