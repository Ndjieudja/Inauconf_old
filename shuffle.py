# --*-- encodng: urf8 --*--
# !/usr/bin/env python3

# =================== Cript Username ====================

from random import randrange

class EncriptAll():
	def __init__(self):

		# define differents var to generate criptfile and keys

		# var from input
		self.account_ = None
		self.password_ = None
			

		# beginning handing process

	# Afther calling this function we return list values we containt keys and crypt values

	def cript(self, target):
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

		# print(values)
		string_int_ = [str(int) for int in values]
		#save_
		self.password_ = "".join(string_int_)

		# Convert to bytearray
		'''a_byte_array = bytearray(values, "utf8")
		byte_list = list()

		# Begin processing
		for byte in a_byte_array:
			binary_representaion = bin(byte)
			byte_list.append(binary_representaion)
			self.password_ = "".join(byte_list)'''

		return self.password_

	
	def uncript(sefl, keys, values):
		print('ok')
		

if __name__ == "__main__":
	EncriptAll()

	
		