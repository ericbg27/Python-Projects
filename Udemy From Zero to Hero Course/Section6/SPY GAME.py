def spy_game(*args):
	sequence = []
	for item in args:
		if item == 0 and len(sequence) < 2:
			sequence.append(item)
		elif item == 7 and len(sequence) == 2:
			sequence.append(item)

	return len(sequence) == 3

print("first: " + str(spy_game(1,2,4,0,0,7,5)))

print("second: " + str(spy_game(1,0,2,4,0,5,7)))

print("third: " + str(spy_game(1,7,2,0,4,5,0)))