from flask import Flask,Blueprint

def create_app():
    app = Flask(__name__)
    
    app.config.from_pyfile('../config.py')
    from .routes import app as app_blueprint
    app.register_blueprint(app_blueprint)

    from .timer import start as timer_start
    timer_start()
    
    from .scheduler import start as scheduler_start
    scheduler_start()
    return app

