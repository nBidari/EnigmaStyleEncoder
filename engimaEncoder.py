# Created by Nima Bidari Janruary 13th 2019
# Consulted by Justin Lee Janruary 13th 2019

import tkinter as tk
import threading

class Rotor:
	
	def __init__(self,rotorOne, rotorTwo, rotorThree, posOne, posTwo, posThree):
		self.rotorOne = rotorOne
		self.rotorTwo = rotorTwo
		self.rotorThree = rotorThree

		self.posOne = posOne
		self.posTwo = posTwo
		self.posThree = posThree

class Plugs:
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

		#Input/Output---------------------------------------------------------------------------------------------------

		self.

		self.root.mainloop()

mainPage = UserInterface()

