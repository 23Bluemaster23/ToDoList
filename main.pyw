import Modules.ui as ui
import Modules.db as db

if __name__ == "__main__":
	db.initDb()
	app = ui.MyApp(0)
	app.MainLoop()