# /usr/bin/env python3
# --*-- conding: utf8 --*--

# File that contain all halding to connect save, and verify 
# password inside data base


import psycopg2
from global_various import global_v


class SGBD:

    def __init__(self, user, db_name, password):

        try:
            self.connected = psycopg2.connect (user=user, dbname=db_name, password=password)
            self.connected.set_session(readonly = False, autocommit = True)
            #create cursor
            #self.cursor = self.connected.cursor()       
            self.echec = 0

        except Exception as err:
            print('fail to connect data base:  \n'
                  'error detected: \n'
                  '{}'.format(err))
            self.echec = 1


    def create_table(self, user_name, mdp):

        with self.connected:
            self.cursor = self.connected.cursor()
            self.cursor.execute(open("shema.sql", "r").read()) 
            querry = "INSERT INTO inauconf (identifiant, iaf_pass)  VALUES (%s, %s)"
            self.cursor.execute(querry, (str(user_name), str(mdp)))

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

        