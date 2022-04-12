import random

def passwordgernerator():
	lowercase=['a','p','f','k','s','n']
	uppercase=['R','Q','Y','H','J','O']
	specialchar=['@','£','&','#','_']
	numbers=['4','6','9','2','7']
	password=random.choice(lowercase)+random.choice(uppercase)+random.choice(specialchar)+random.choice(numbers)

	password=password+password
	return password
