import json

str = '{"name":"孙嘉乐"}'
obj = json.loads(str)
print(type(obj))

obj_str = json.dumps(obj,ensure_ascii=False)
print(obj_str)

json.dump(obj,open("namelist.txt","w",encoding="utf-8"),ensure_ascii=False)
obj2 = json.load(open("namelist.txt",encoding="utf-8"))
print(obj2)