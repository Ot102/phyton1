Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from flask import Flask
... app = Flask(__name__)
... 
... @app.route('/')
... def home():
...     return "Тавтай морилно уу!"
... 
... if __name__ == '__main__':
...     app.run(debug=True)
... 
SyntaxError: multiple statements found while compiling a single statement
