# use map(): convert a list of lowercase strings to uppercase(lists of 7 days).

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

print(list(map(lambda day: day.upper(), days)))

