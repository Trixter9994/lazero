# what to do?
# import jinja2
from jinja2 import Template
# even if it is trash, we still have to let it to learn.
# well, that is because we are using ak!
# well, you want to create a graph, or a dice like thing?
# put a function into it?
# how is that possible?
tpl = Template('''{{ type_name }}=lambda x:x*10''')
render_tpl = tpl.render(type_name="hello_world")
# mod = SourceModule(render_tpl)
print(render_tpl)
# print(tpl)
# a template memory?
# what the fuck?
# print(mod)