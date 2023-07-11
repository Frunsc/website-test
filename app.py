from flask import Flask

appp = Flask(__name__)

@appp.route("/")
def home():
   return "<p>HELLO<p>"

if __name__ == "__main__":
  appp.run(host= "0.0.0.0", debug= True)