#enconding=utf-8
print("hello world!")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
# for name in sorted(favorite_languages.keys()):
for name in sorted(favorite_languages.values()):
	print(name.title() + ", thank you for taking the poll.")

#6-4
favor_rivers = {
	'china' : "HuangHe River",
	'U.S':"密西西比河",
	'越南':'湄公河',
	'England':'莱茵河'
}

print(favor_rivers)
for mykey in favor_rivers.keys():
	print('The ' + favor_rivers[mykey] + ' runs through '+ mykey +'.')