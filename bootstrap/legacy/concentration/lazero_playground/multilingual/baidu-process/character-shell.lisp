(ql:quickload :inferior-shell)
(print (inferior-shell:run "ls" :output :string))
(quit)
