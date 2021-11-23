# --*-- encodng: urf8 --*--
# !/usr/bin/env python3

# =================== Cript Username ====================

import sqlite3, psycopg2, re

class EncriptAll():
	def __init__(self):

		# define differents var to generate criptfile and keys

		# var from input
		self.account_ = None
		self.username_ = None
		self.password_ = None

		# var to cript file and get key
		self.key_val = list()
		self.key = list()
		self.values = list()
		
		self.get_key_values('Gabriel')
		print(self.key, self.values)
		

		# beginning handing process

# Afther calling this function we return list values we containt keys and crypt values

	def get_key_values(self, target):
		# create dic var we contaitn first value and keys to uncrypt values

		for el in range(len(target)):
			if ord(target[el]) < 10:
				self.key_val.append((chr(97), ord(target[el])))
			elif ord(target[el]) < 100:
				self.key_val.append((chr(99), ord(target[el])))
			else: self.key_val.append((chr(100), ord(target[el])))

		for el in self.key_val:
			self.key.append(el[0])
			self.values.append(el[1])

		self.key = "".join(self.key)
		string_int_ = [str(int) for int in self.values]
		self.values = "".join(string_int_)

	
	def uncript(sefl, keys, values):
		

if __name__ == "__main__":
	EncriptAll()

	
		