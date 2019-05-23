import json

data = {
		'user' : '',
		'winrate' : 0,
		'plays' : 0,
		'mostUsedOption' : '',
		'timesUsedPaper' : 0,
		'timesUsedRock' : 0,
		'timesUsedScissors' : 0,
		}

class DataManager:
	#Loads the data from the "Data.txt"
	def loadData():

		try:
			_data = open('data.txt', 'rb')
			read_data = _data.read()
			return read_data
		except Exception:
			print('\nNo data found!')
			print("Do you want to create a new game?\n\n1) Yes\n2) No")

			response = str(input())

			if(response == "1"):
				newGame()
			elif(response == "2"):
				initMessage()

			return []

	#Creates a new blank "Data.txt"
	def newGame():
		try:
			_data = open('data.txt', 'r')
			print("There is previous data, do you want to overwrite it?\n\n1) Yes\n2) No")
			response = int(input())

			if(response == 1):
				overwriteGame()
			elif(response == 2):
				initMessage()

		except Exception:
			overwriteGame()


	#Overwrites the content of "Data.txt"
	def overwriteGame():

		print('Write your username')

		data['user'] = str(input())

		with open('data.txt', 'w') as _data:
			_data.write(json.dumps(data))


def initMessage():

	print('\nHello! welcome to Rock, Paper, Scissors!\n')
	print('Select an option: \n\n')
	print('1) Load Game\n2) New Game')

	try:
		option = int(input())

		if(option == 1):
			data = DataManager.loadData()
		elif(option == 2):
			DataManager.newGame()
		else:
			print("No valid input!\n")
			initMessage()

	except Exception:
		print("No valid input!\n")
		initMessage()

initMessage()