# --*-- encodng: urf8 --*--
# !/usr/bin/env python3

# =================== Cript Username ====================

import sqlite3, psycopg2, re
import getpass
from random import randrange

from sgbd import SGBD
from global_various import global_v

class EncriptAll():
	def __init__(self):

		# define differents var to generate criptfile and keys

		# var from input
		self.account_ = None
	

		while True:
			try:
				self.username = input("usuer name: ")
				self.password_ = getpass.getpass("password: ")
				if len(self.password_) < 10:
					print("============= Error =================")
					print(" 	Minimal character is 10")
					print("\n=========== Try againt =========")

				else: 
					print("\n=========== Done ==============")
					break

			except Exception as error:
				print(error)


		self.get_key_values("self.password_")

		save_data = SGBD(global_v.user, global_v.dbname, global_v.passsword)
		save_data.create_table(self.username, self.password_)
		save_data.enregistre()
		save_data.sortie()

		

		# beginning handing process

	# Afther calling this function we return list values we containt keys and crypt values

	def get_key_values(self, target):
		# create dic var we contaitn first value and keys to uncrypt values

		# __init__ variours
			
		key_val = list()
		key = list()
		values = list()
		
		container_cript = list()
		for el in range(len(target)):
			if ord(target[el]) < 10:
				key_val.append((ord(target[el]), randrange(1, 10)))

			elif ord(target[el]) < 100:
				key_val.append((ord(target[el]), chr(randrange(10, 100))))

			else: key_val.append((ord(target[el]), chr(randrange(100, 1000))))

		for el in key_val:
			values.append(el[1])
			values.append(el[0])

		print(values)
		string_int_ = [str(int) for int in values]
		#save_
		values = "".join(string_int_)

		# Convert to bytearray
		a_byte_array = bytearray(values, "utf8")
		byte_list = list()

		# Begin processing
		for byte in a_byte_array:
			binary_representaion = bin(byte)
			byte_list.append(binary_representaion)
			self.passsword_ = "".join(byte_list)

		print(self.passsword_)

	
	def uncript(sefl, keys, values):
		print('ok')
		

if __name__ == "__main__":
	EncriptAll()

	
		