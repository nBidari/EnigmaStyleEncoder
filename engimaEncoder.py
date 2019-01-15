# Created by Nima Bidari Janruary 13th 2019
# Consulted by Justin Lee Janruary 13th 2019

import tkinter as tk
import threading

alphabet = "ABCDEFGHIJKMNOPQRSTUVWXYZ"

class Rotor:
	
	def __init__(self,numRotorOne, numRotorTwo, numRotorThree,rotorOne, rotorTwo,rotorThree, rotorFour, posOne, posTwo, posThree):
		self.numRotorOne = numRotorOne
		self.numRotorTwo = numRotorTwo
		self.numRotorThree = numRotorThree

		self.numrotorOneRotate = 0
		self.numrotorTwoRotate = 0
		self.numrotorThreeRotate = 0

		self.rotorOne = "JGDQOXUSCAMIFRVTPNEWKBLZYH"
		self.rotorTwo = "NTZPSFBOKMWRCJDIVLAEYUXHGQ"
		self.rotorThree = "JVIUBHTCDYAKEQZPOSGXNRMWFL"
		self.rotorFour = "QYHOGNECVPUZTFDJAXWMKISRBL"
		self.rotorFive = "QWERTZUIOASDFGHJKPYXCVBNML"

		self.posOne = posOne
		self.posTwo = posTwo
		self.posThree = posThree

	def rotorEncode:
		print("Encode")
	def rotorSpin:
		print("Spin")

class Plugboard:
	pass

class UserInterface:

	def __init__(self):
		#self.output = outputStr

		self.root = tk.Tk()
		self.root.title("Enigma-Esque Encoding Machine")
		self.root.configure(background = "#374140")

		#Rotors---------------------------------------------------------------------------------------------------------
		self.rotorFrame = tk.LabelFrame(self.root, text = "Rotor #")
		self.rotorFrame.config(background = "#374140", relief = "solid")
		self.rotorFrame.grid(row = 0, column = 0, padx = 10, pady = 5)

		self.rotorOneSpin = tk.Spinbox(self.rotorFrame, from_ = 0, to = 5, width = 3)
		self.rotorOneSpin.config(background = "#374140", fg = "#DC3522")
		self.rotorOneSpin.grid(row = 1, column = 0, padx = 10, pady = 5)

		self.rotorTwoSpin = tk.Spinbox(self.rotorFrame, from_ = 0, to = 5, width = 3)
		self.rotorTwoSpin.config(background = "#374140", fg = "#DC3522")
		self.rotorTwoSpin.grid(row = 1, column = 1, padx = 10, pady = 5)

		self.rotorThreeSpin = tk.Spinbox(self.rotorFrame, from_ = 0, to = 5, width = 3)
		self.rotorThreeSpin.config(background = "#374140", fg = "#DC3522")
		self.rotorThreeSpin.grid(row = 1, column = 2, padx = 10, pady = 5)


		#-------------------------------------------------------------------------------

		self.posFrame = tk.LabelFrame(self.root, text = "Rotor Pos")
		self.posFrame.config(background = "#374140", relief = "solid")
		self.posFrame.grid(row = 1, column = 0, padx = 10, pady = 5)

		self.posOneSpin = tk.Spinbox(self.posFrame, from_=0, to = 26, width = 3)
		self.posOneSpin.config(background = "#374140", fg = "#DC3522")
		self.posOneSpin.grid(row = 0, column = 0, padx = 10, pady = 5)

		self.posTwoSpin = tk.Spinbox(self.posFrame, from_=0, to = 26, width = 3)
		self.posTwoSpin.config(background = "#374140", fg = "#DC3522")
		self.posTwoSpin.grid(row = 0, column = 1, padx = 10, pady = 5)

		self.posThreeSpin = tk.Spinbox(self.posFrame, from_=0, to = 26, width = 3)
		self.posThreeSpin.config(background = "#374140", fg = "#DC3522")
		self.posThreeSpin.grid(row = 0, column = 2, padx = 10, pady = 5)

		#Plugboard------------------------------------------------------------------------------------------------------

		self.plugWidth = 3

		self.plugFrame = tk.LabelFrame(self.root, text = "Plugboard")
		self.plugFrame.config(background = "#374140", fg = "#fffdd0", relief = "solid")
		self.plugFrame.grid(row = 2, column = 0, rowspan = 6, padx = 10, pady = 5)

		#-------------------------------------
		self.entOne = tk.Entry(self.plugFrame, width = self.plugWidth)
		self.entOne.config(background = "#374140", fg = "#DC3522")
		self.entOne.grid(row = 0, column = 0, padx = 10, pady = 5)

		self.entTwo = tk.Entry(self.plugFrame, width = self.plugWidth)
		self.entTwo.config(background = "#374140", fg = "#DC3522")
		self.entTwo.grid(row = 0, column = 1, padx = 10, pady = 5)

		self.entThree = tk.Entry(self.plugFrame, width = self.plugWidth)
		self.entThree.config(background = "#374140", fg = "#DC3522")
		self.entThree.grid(row = 0, column = 2, padx = 10, pady = 5)
		
		#-------------------------------------
		self.entFour = tk.Entry(self.plugFrame, width = self.plugWidth)
		self.entFour.config(background = "#374140", fg = "#DC3522")
		self.entFour.grid(row = 1, column = 0, padx = 10, pady = 5)

		self.entFive = tk.Entry(self.plugFrame, width = self.plugWidth)
		self.entFive.config(background = "#374140", fg = "#DC3522")
		self.entFive.grid(row = 1, column = 1, padx = 10, pady = 5)

		self.entSix = tk.Entry(self.plugFrame, width = self.plugWidth)
		self.entSix.config(background = "#374140", fg = "#DC3522")
		self.entSix.grid(row = 1, column = 2, padx = 10, pady = 5)

		#-------------------------------------
		self.entSeven = tk.Entry(self.plugFrame, width = self.plugWidth)
		self.entSeven.config(background = "#374140", fg = "#DC3522")
		self.entSeven.grid(row = 2, column = 0, padx = 10, pady = 5)

		self.entEight = tk.Entry(self.plugFrame, width = self.plugWidth)
		self.entEight.config(background = "#374140", fg = "#DC3522")
		self.entEight.grid(row = 2, column = 1, padx = 10, pady = 5)

		self.entNine = tk.Entry(self.plugFrame, width = self.plugWidth)
		self.entNine.config(background = "#374140", fg = "#DC3522")
		self.entNine.grid(row = 2, column = 2, padx = 10, pady = 5)

		#-------------------------------------
		self.entTen = tk.Entry(self.plugFrame, width = self.plugWidth)
		self.entTen.config(background = "#374140", fg = "#DC3522")
		self.entTen.grid(row = 3, column = 1, padx = 10, pady = 5)


		#Input/Output---------------------------------------------------------------------------------------------------

		self.inputEnt = tk.Text(self.root, background = "black", foreground = "lime",
									height = 10, width = 65)
		self.inputEnt.config(highlightbackground = "#074C0A")
		self.inputEnt.grid(row = 0, column = 1, rowspan = 3, sticky = 'NESW', padx = 10, pady = 5)

		self.submitbtn = tk.Button(self.root, text = "Encode", width = 25, height = 2)
		self.submitbtn.config(background = "#DADFDF", relief = "raised", highlightbackground = "#374140")
		self.submitbtn.grid(row = 4, column = 1, sticky = 'NESW',padx = 10, pady = 5)

		self.outputEnt = tk.Text(self.root, background = "black", foreground = "lime",
									height = 10, width = 65)
		self.outputEnt.config(highlightbackground = "#074C0A")
		self.outputEnt.grid(row = 5, column = 1, rowspan = 3, sticky = 'NESW', padx = 10, pady = 5)

		#---------------------------------------------------------------------------------------------------------------

		self.root.mainloop()

mainPage = UserInterface()

print(Rotor.rotorOne)

