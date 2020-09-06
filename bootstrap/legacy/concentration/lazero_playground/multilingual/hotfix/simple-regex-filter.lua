file=io.open("unbash6.log","r")
function resolve (n)
	-- print(n)
	for word in string.gmatch(n, 'http://www%.baidu%.com/link%?url=[^%""]+') do
		print(word)
	end
end
-- print(file:read())
variable=""
while true  do
	variable=file:read()
	-- print(variable)
	if variable ~=nil
	then
		resolve(variable)
		-- name with variable
	else
		break
	end
	-- to make sure there isn't any silly nil
end
-- it will only return one line at a time
-- print(file:flush())
-- does this work?
-- no it does not work
-- use colon to transfer the file object to the method.
file:close()
