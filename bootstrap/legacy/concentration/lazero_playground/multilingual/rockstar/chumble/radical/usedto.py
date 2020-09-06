import uuid, ast

fuck=uuid.uuid4().hex
print(ast.literal_eval("0x"+fuck.lower()))
