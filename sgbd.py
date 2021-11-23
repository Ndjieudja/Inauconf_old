# /usr/bin/env python3
# --*-- conding: utf8 --*--

# File that contain all halding to connect save, and verify 
# password inside data base


import psycopg2
from global_various import global_v


class SGBD:

    def __init__(self, user, db_name, password):

        self.connection = None
        self.requette = None
        self.cursor = None

        try:
            self.conection = psycopg2.connect(user=user, dbname=db_name, password=password)

            #create cursor
            self.cursor = self.conection.cursor()       
            print('connected sucessful')
            self.echec = 0

        except Exception as err:
            print('fail to connect data base:  \n'
                  'error detected: \n'
                  '{}'.format(err))
            self.echec = 1

    def create_table(self, username, password):


        with self.connection as cursor:
            cursor.execute(open("shema.sql", "r").read())

        #print((name, title))

        self.cursor.execute('''INSERT OR IGNORE INTO inauconf (user_name, password)
                VALUES ( ? , ?)''', ( username, password, )) 
        '''cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
        user_id = cur.fetchone()[0]'''

        # cur.execute('''INSERT OR IGNORE INTO Course (title)
        #        VALUES ( ? )''', ( title, ) )
        # cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
        # course_id = cur.fetchone()[0]

        # cur.execute('''INSERT OR REPLACE INTO Member
        #        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        #        (user_id, course_id , 0))

        # cur.execute('''SELECT User.name, Course.title, Member.role FROM 
        # User JOIN Member JOIN Course 
        # ON User.id = Member.user_id AND Member.course_id = Course.id
        # ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
        # ''')

        # print(list(cur))


        '''self.requette = ('CREATE TABLE {}(nom text, age INTEGER)'.format(table))
        self.cursor.execute(self.requette)'''


    def enregistre(self):
        choix=input("voulez vous enregistre les modification o/n: ")
        if choix == 'o' or  choix == 'O':
            self.conection.commit()
        else:
            self.echec=1

    def sortie(self):
        self.cursor.close()
        self.conection.close()

        