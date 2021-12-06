# usr/bin/env python3
# --*-- coding: utf8 --*--



import sqlite3, psycopg2, re
import getpass

from sgbd import SGBD
from global_various import global_v
from shuffle import EncriptAll



while True:
		try:
			user_name = input("usuer name: ")
			mdp = getpass.getpass("password: ")
			if len(mdp) < 10:
				print("============= Error =================")
				print(" 	Minimal character is 10")
				print("\n=========== Try againt =========")

			else: 
				print("\n=========== Done ==============")
				break

		except Exception as error:
			print(error)

encript = EncriptAll()
encript.cript(mdp)

try:
	save_data = SGBD(global_v.user, global_v.dbname, global_v.password)
	save_data.create_table(user_name, encript.password_)

			
except Exception as error:
	print(error)