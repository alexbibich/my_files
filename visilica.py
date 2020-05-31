import os

def hangman(word):
	wrong = 0
	stages = ["",
		"______      ",
		"|     |     ",
		"|     |     ",
		"|     O     ",
		"|    /|\\    ",
		"|    / \\    ",
		"|           "
	]
	rletters = list(word)
	board = ["__"] * len(word)
	win = False
	os.system("cls")
	print("\n\nДобро пожаловать на казнь!")
	print(" ".join(board))
	us = list()
	while wrong < len(stages) - 1:
		print("\n")
		msg = "Введите букву: "
		char = input(msg)

		if len(char) != 1:
			print("Введено слово!")
			continue
		else:
			if char in us:
				print('Такая буква уже вводилась!')
				continue 
			else:
				us += char
		if char in rletters:
			while char in rletters:
				cind = rletters.index(char)
				board[cind] = char
				rletters[cind] = '$'

		else:
			wrong += 1
		print((" ".join(board)))
		e = wrong + 1
		print("\n".join(stages[0:e]))
		if "__" not in board:
			print("Вы выиграли! Было загадано слово: ")
			print(" ".join(board))
			win = True
			break
	if not win:
		print("Вы проиграли! Было загадано слово: {}".format(word))

while True:
	a = input("Введите слово: ")
	lol = 0
	for kek in a:
		try:
			kek = int(kek)
			lol = 1
		except:
			pass
	if lol != 1:
		hangman(a)
	else:
		print("Введено число!")
		continue

