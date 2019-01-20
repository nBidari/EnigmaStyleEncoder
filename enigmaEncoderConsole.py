rotorsInit = [["P","E","Z","U","O","H","X","S","C","V","F","M","T","B","G","L","R","I","N","Q","J","W","A","Y","D","K"], 
		  	  ["Z","O","U","E","S","Y","D","K","F","W","P","C","I","Q","X","H","M","V","B","L","G","N","J","R","A","T"], 
		  	  ["E","H","R","V","X","G","A","O","B","Q","U","S","I","M","Z","F","L","Y","N","W","K","T","P","D","J","C"],
		  	  ["I","M","E","T","C","G","F","R","A","Y","S","Q","B","Z","X","W","L","H","K","D","V","U","P","O","J","N"],
		  	  ["Q","W","E","R","T","Z","U","I","O","A","S","D","F","G","H","J","K","P","Y","X","C","V","B","N","M","L"]
		 ]

rotors = [["P","E","Z","U","O","H","X","S","C","V","F","M","T","B","G","L","R","I","N","Q","J","W","A","Y","D","K"], 
		  ["Z","O","U","E","S","Y","D","K","F","W","P","C","I","Q","X","H","M","V","B","L","G","N","J","R","A","T"], 
		  ["E","H","R","V","X","G","A","O","B","Q","U","S","I","M","Z","F","L","Y","N","W","K","T","P","D","J","C"],
		  ["I","M","E","T","C","G","F","R","A","Y","S","Q","B","Z","X","W","L","H","K","D","V","U","P","O","J","N"],
		  ["Q","W","E","R","T","Z","U","I","O","A","S","D","F","G","H","J","K","P","Y","X","C","V","B","N","M","L"]
		 ]
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#----Shift-and-AlphaNum-Function------------------------------------------------------------
def shift(l, n):
	return l[n:] + l[:n]

def inputAlphaNum(inputChar):
	inputNum = 0

	for j in range(len(alphabet)):
		if inputChar == alphabet[j]:
			inputNum = j
		else:
			pass
	return inputNum

#----Input----------------------------------------------------------------------------------
rotorMod1 = int(input("What is your first rotor? "))
rotorMod2 = int(input("What is your second rotor? "))
rotorMod3 = int(input("What is your third rotor? "))
print("\n")

rotorPos1 = int(input("What is your first rotor's position? "))
rotorPos2 = int(input("What is your second rotor's position? "))
rotorPos3 = int(input("What is your third rotor's position? "))
print("\n")

initAlpha = ""
for i in range(0,26):
	if i != 26:
		initAlpha += alphabet[i] + str(i) + " | "
	else:
		initAlpha += alphabet[i] + str(i)

print(initAlpha)
print("\n")

plugboardInput = input("Your plugboard (no repeated letters | Use numbers and seperate by spaces and dashes): ")
print("\n")

rotors[rotorMod1] = shift(rotors[rotorMod1],-rotorPos1)
rotors[rotorMod2] = shift(rotors[rotorMod2],-rotorPos2)
rotors[rotorMod2] = shift(rotors[rotorMod3],-rotorPos3)

message = input("What is your message? ").split()
outputStr = ""

for l in range(len(message)):
	if message[l] == " ":
		message[l] = ""
	else:
		pass


def machine(inputLetter):
	#Rotor1
	localInputNum = inputAlphaNum(inputLetter)
	inputLetter = rotors[rotorMod1][localInputNum]


	#Shift
	rotors[rotorMod1] = shift(rotors[rotorMod1], -1)

	#Rotor2
	localInputNum = inputAlphaNum(inputLetter)
	inputLetter = rotors[rotorMod2][localInputNum]

	#Shift
	rotors[rotorMod1] = shift(rotors[rotorMod2], -1)

	#Rotor3
	localInputNum = inputAlphaNum(inputLetter)
	inputLetter = rotors[rotorMod3][localInputNum]

	#Shift
	rotors[rotorMod1] = shift(rotors[rotorMod3], -1)

	#Plugboard

	#Output
	return inputLetter

for i in range(len(message)):
	outputStr += machine(message[i])

print(outputStr)






