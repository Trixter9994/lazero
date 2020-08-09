-- i wanna a unity.
function mysplit (inputstr, sep)
        if sep == nil then
                sep = "%s"
        end
        local t={}
        for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
                table.insert(t, str)
        end
        return t
end
-- you could train a module to classify things to create regex builder.
-- remember to tackle down things.
-- you can also read through the manual, or collect online regex and build hierachy tree for it.
-- the core is the verification.
geohot=io.popen("python latte.py")
-- we are trying to apply advanced mathematics to our fucking project.
-- what a shame. you couldn't do this by using the computer.
result = geohot:read("*a")
geohot:close()
nk=mysplit(result,"\n")
mk=" "
for k,f in ipairs(nk) do
	mk=mk..'"'..f..'" '
end
-- print(mk)

geohot=io.popen("regexgen"..mk)
result = geohot:read("*a")
geohot:close()
print(result)

