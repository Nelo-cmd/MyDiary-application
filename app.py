#import flask
from flask import Flask
from flask_session import Session
from datetime import timedelta
from flask_wtf.csrf import CSRFProtect


#define app
app= Flask(__name__)
app.config['SECRET_KEY'] = "nelogirl"
app.config["SESSION_PERMANENT"] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
csrf = CSRFProtect(app)

#cursor.execute("CREATE TABLE randomtable(myname,yourname)")
#register auth and views blueprints
from auth import auth
app.register_blueprint(auth, url_prefix = "/")

from views import views
app.register_blueprint(views, url_prefix = "/")


#run app
if __name__ == "__main__":
    app.run(host= '0.0.0.0', port= 7000,  debug = True)


