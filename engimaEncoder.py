# Created by Nima Bidari Janruary 13th 2019
# Consulted by Justin Lee Janruary 13th 2019

import tkinter as tk

class Rotor:
	
	def __init__(self,rotorOne, rotorTwo, rotorThree):
		self.rotorOne = rotorOne
		self.rotorTwo = rotorTwo
		self.rotorThree = rotorThree

class Plugs:
	pass

class UserInterface:

	def __init__(self,outputStr):
		self.output = ""

		self.root = tk.Tk()
		self.root.title("Enigma-Esque Encoding Machine")
		self.root.configure(background = "#374140")

		self.
