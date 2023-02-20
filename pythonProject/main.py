import re
s = "Solomon Prabu"
x = re.findall("[o]",s)
print(x)
print("\u0332".join(x))