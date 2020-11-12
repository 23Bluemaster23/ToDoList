import sqlite3,os

path = 'DDBB'
if os.path.isdir(path) != True:
	os.mkdir(path)

taskCon = sqlite3.connect('DDBB/db.db')

taskCur = taskCon.cursor()

def initDb():

	taskCur.execute("""CREATE TABLE IF NOT EXISTS DOTASK(ID INTEGER PRIMARY KEY AUTOINCREMENT,Task TEXT NOT NULL)""")

	taskCur.execute("""CREATE TABLE IF NOT EXISTS DOINGTASK(ID INTEGER PRIMARY KEY AUTOINCREMENT,Task TEXT NOT NULL)""")

	taskCur.execute("""CREATE TABLE IF NOT EXISTS DIDTASK(ID INTEGER PRIMARY KEY AUTOINCREMENT,Task TEXT NOT NULL)""")

	taskCon.commit()

def readData(Table):
	
	taskTable = []

	DoHeader = []


	if Table == 'DO':
		
		data = taskCur.execute('SELECT TASK FROM DOTASK')

		

		taskCon.commit()

		for value in data:

			taskTable.append(value[0])
	
	elif Table == 'DOING':

		data = taskCur.execute('SELECT TASK FROM DOINGTASK')

		taskCon.commit()

		for value in data:

			taskTable.append(value[0])

	elif Table == 'DID':

		data = taskCur.execute('SELECT TASK FROM DIDTASK')

		

		taskCon.commit()

		for value in data:

			taskTable.append(value[0])

	return taskTable

def createTask(text):
	
	taskCur.execute("INSERT INTO DOTASK VALUES(NULL,?)",(text,))
	
	taskCon.commit()

def doingTask(task):

	ID = taskCur.execute('SELECT ID FROM DOTASK WHERE TASK = ?',(task,))

	for i in ID:
		ID = i[0]
	taskCur.execute("DELETE FROM DOTASK WHERE ID = ?",(ID,))

	taskCur.execute("INSERT INTO DOINGTASK VALUES(NULL,?)",(task,))

	taskCon.commit()

def didTask(task):

	ID = taskCur.execute('SELECT ID FROM DOINGTASK WHERE TASK = ?',(task,))

	for i in ID:
		ID = i[0]
	taskCur.execute("DELETE FROM DOINGTASK WHERE ID = ?",(ID,))

	taskCur.execute("INSERT INTO DIDTASK VALUES(NULL,?)",(task,))

	taskCon.commit()

def clearTask():

	taskCur.execute('DELETE FROM DIDTASK')

	taskCon.commit()