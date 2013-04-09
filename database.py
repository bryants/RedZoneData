#!/usr/bin/python

import MySQLdb





def add(datas):
	# Open database connection
	db = MySQLdb.connect("localhost","joe","asdf","joe" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	for data in datas:
	# execute SQL query using execute() method.
		cursor.execute("SELECT * FROM words WHERE word_name=\'%s\'" % (data['word']))
		result = cursor.fetchone()
		if str(result) == 'None':
			cursor.execute("INSERT INTO words (word_name) VALUES (\"%s\")" %(data['word']))
			db.commit()

		cursor.execute("SELECT * FROM words WHERE word_name=\'%s\'" % (data['word']))
		result = cursor.fetchone()

		cursor.execute("SELECT * FROM times WHERE word_id=\'%s\' AND date=\'%s\'" % (result[0],data['time']))
		result1 = cursor.fetchone()
		if str(result1) == 'None':
			cursor.execute("INSERT INTO times (word_id, date) VALUES (\'%s\',\'%s\')"%(result[0],data['time']))
			db.commit()
		cursor.execute("SELECT * FROM times WHERE word_id=\'%s\' AND date=\'%s\'" % (result[0],data['time']))
		result1 = cursor.fetchone()

		cursor.execute("SELECT * FROM locations WHERE time_id=\'%s\' AND lat=\'%s\' AND `long`=\'%s\'" %(result1[0],data['lat'],data['long']))
		result2 = cursor.fetchone()
		if str(result2) == 'None':
			cursor.execute("INSERT INTO locations (time_id, sentiment, volume, lat, `long`) VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')"%(result1[0],data['sentiment'],data['volume'],data['lat'],data['long']))
		db.commit()
	



	# disconnect from server
	db.close()

