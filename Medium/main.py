from flask import Flask, make_response, render_template

app = Flask(__name__)

COOKIE_CONTENTS = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>-----.>++++++++.+.++.++++.+.<<++.>+++++++++++++++++++.>------------.---.+++++++++++++.-------------.<<+.-.>---.<++++++++++++++++++.+++++++.>>+++++++++++++++.-----------------.<-----------.++++++++.>+++++++++++++++++++.<+++++++++++.<------.>>--.<<+++++++++++++++++.+++++++++.---------.--.++++++++++.+.>-----.<+.>>--------------.<..<------------.>-----.-----.<++++.>++++++++.<----.>+++.>++++++++.<<------------------.+++++++++++++."

# Flag is CompSoc{C00K13_M0N$TAR}
# In base 64 that's Q29tcFNvY3tDMDBLMTNfTTBOJFRBUn0=
# The Phrase "Almost There! Q29tcFNvY3tDMDBLMTNfTTBOJFRBUn0=" is the COOKIE_CONTENTS of FLAG in brainfucl


@app.route('/')
def index():
    response = make_response(render_template('index.html'))    
    response.set_cookie('flag-🧠💦', COOKIE_CONTENTS, httponly=False)
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0")