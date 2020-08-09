(ql:quickload :inferior-shell)
(print (inferior-shell:run "echo 'super hot'" :output :string))
(quit)
