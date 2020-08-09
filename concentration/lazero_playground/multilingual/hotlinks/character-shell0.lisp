(ql:quickload :inferior-shell)
(print (inferior-shell:run "node node-batch.js 'super hot'" :output :string))
(quit)
