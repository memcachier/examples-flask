from flask import Flask

from task_list import create_app

application = create_app()
if __name__ == "__main__":
	application.run()
