# var
cats = 2
dogs = 5
horses = 1
recipe = "a recipe isn't a list of ingredients."
# list
a_counts = [cats, dogs, horses]
cat_n = ['w', 'r']
dog_n = ['j', 's', 'e', 'l', 'f']
horse_n = ['m']
a_names = [cat_n, dog_n, horse_n]
# dic
an_counts = {'cats': 2, 'dogs': 5, 'horses': 1}
an_counts['dogs']
an_names1 = {
    'cats': ['w', 'r'],
    'dogs': ['j', 's', 'e', 'l', 'f'],
    'horses': ['m']
}
an_names2 = {
    'cats': cat_n,
    'dogs': dog_n,
    'horses': horse_n
}
an_names1['cats']
an_names2['dogs']
# met
filename = 'budget.csv        '
filename = filename.strip()
print filename
filename = 'budget.scv'
filename = filename.upper()
print filename
dog_names = ['j', 's', 'e', 'l', 't']
dog_names.remove('e')
animal_counts = {'horses': 1, 'cats': 2, 'dogs': 5, 'snakes': 0}
animal_counts.keys()
animal_counts['dogs']
dogs1 = animal_counts['dogs']
# tool
print dogs1
type(20011)
type('20011')
dir('cat,dog,horse')
'cat,dog,horse'.split(',')
dir(['cat', 'dog', 'horse'])
animals = ['cat', 'dog', 'horse']
animals.reverse()
print animals
animals.sort()
print animals
animals = 'cat,dog,horse'
help(animals.split)
