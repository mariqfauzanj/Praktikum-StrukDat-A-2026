# 1.
sovetskytank = {
  "name": "T-34",
  "type": "Medium",
  "year": 1934
}
print(sovetskytank)

# dict item
sovetskytank = {
  "name": "T-34",
  "type": "Medium",
  "year": 1934
}
print(sovetskytank["name"])

# induplicable
aircraft = {
  "name": "P-51 Mustang",
  "year": 1964,
  "year": 2006
}
print(aircraft)

# type()
sovetskytank = {
  "name": "T-34",
  "type": "Medium",
  "year": 1934
}
print(type(sovetskytank))

# 2. akses dict
# get
sovetskytank =	{
  "name": "T-34",
  "type": "Medium",
  "year": 1934
}
x = sovetskytank.get("type")
print(x)

# keys
sovetskytank = {
  "name": "T-34",
  "type": "Medium",
  "year": 1934
}
x = sovetskytank.keys()
print(x)

# values
sovetskytank = {
  "name": "T-34",
  "type": "Medium",
  "year": 1934
}
x = sovetskytank.values()
print(x)

# items
sovetskytank = {
  "name": "T-34",
  "type": "Medium",
  "year": 1934
}
x = sovetskytank.items()
print(x)

# update
sovetskytank = {
  "name": "T-34",
  "type": "Medium",
  "year": 1934
}
sovetskytank.update({"modifier": "Stabilizer"})
print(sovetskytank)

# nested
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}