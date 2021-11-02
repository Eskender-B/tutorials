from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/hello')
def hello_aau():
   return "Hello AAU"

@app.route('/viewht')
def show_html():
    return """<!DOCTYPE html>
<html>
<body>

<h3 style="color:Tomato;">Hello World</h3>

<p style="color:DodgerBlue;">Lorem ipsum</p>

<p style="color:MediumSeaGreen;">Ut wisi </p>

</body>
</html>"""

if __name__ == '__main__':
   app.run()
