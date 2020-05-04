from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello Stefano! Here is a secure EB application :-) "


if __name__ == "__main__":
    application.debug = True
    application.run()
