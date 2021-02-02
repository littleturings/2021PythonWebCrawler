import re


str = "I study python 3.8 every_day"

# ---------- match ----------
m1 = re.match(r"I", str)
m2 = re.match(r"\w", str)
m3 = re.match(r".", str)
m4 = re.match(r"\S", str)
print(m1.group())
print(m2.group())
print(m3.group())
print(m4.group())

# ---------- search ----------
s1 = re.search(r"study", str)
s2 = re.search(r"s\w+", str)
s3 = re.search(r"I (\w+)", str)
s4 = re.search(r"y", str)
print(s1.group())
print(s2.group())
print(s3.group())
print(s4.group())

# ---------- findall ----------
f1 = re.findall(r"y", str)
f2 = re.findall(r"python 3.8", str)
f3 = re.findall(r"p\w+ 3.8",str)
f4 = re.findall(r"p.+\d", str)
print(f1)
print(f2)
print(f3)
print(f4)

# ---------- sub ----------
su1 = re.sub(r"every_day", r"EveryDay", str)
su2 = re.sub(r"e\w+", r"EveryDay", str)
print(su1)
print(su1)

# ---------- test ----------
str1 = "<div><a class='title' href='https://www.baidu.com'>百度baidu</a></div>"

t1 = re.findall(r"百度",str1)
t2 = re.findall(r"[\u4e00-\u9fa5]",str1)
t3 = re.findall(r"[\u4e00-\u9fa5]+\w+",str1)
t4 = re.findall(r"<a class='title' href='https://www.baidu.com'>(.*)</a>",str1)
t5 = re.sub(r"div","span",str1)
t6 = re.sub(r"<div>(<a.+a>)</div>","<span>\1<\span>",str1)
print(t6)
