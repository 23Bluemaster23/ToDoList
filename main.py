
#!/usr/bin/python3

import Modules.ui as UI

import Modules.db as DB

def main():

	DB.initDb()
	
	import sys

	app = UI.QtWidgets.QApplication(sys.argv)

	MainWindow = UI.QtWidgets.QMainWindow()

	ui = UI.Ui_MainWindow()

	ui.setupUi(MainWindow)

	MainWindow.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	
	main()
