from Read import Read
from InternalProcessing import IP
from Tell import Tell
from NNGestor import NNG
from Be import Be
from flask import Flask, render_template, request

def main(inp):
    NN = list() # NN list (Network Neurons)
    nng = NNG(NN)
    nng.load()
    NN = nng.nn
    be = Be(NN)
    be.load()
    be.bump_normalizer()

    read = Read()
    ip = IP(NN, be)
    tell = Tell()
    ans = ">> "

    if inp != "\exit":
        read.input = inp
        read.read()
        ip.int_input = read.IP_int_output
        ip.out_input = read.IP_out_output
        ip.processing()
        tell.input = ip.tell_output
        ans = ">> "+str(tell.answer())
        read.clear()
        ip.clear()
        tell.clear()
    return ans

app = Flask(__name__)

# Home page and post request
@app.route('/', methods=['GET', 'POST'])
def refresh_results():
    if request.method == 'POST':
        if request.form["text"] != "":
            inp = request.form["text"]
            return render_template('home.html', main=str(">> "+inp+"\n")+str(main(inp)), inp="")
    inp = ""
    return render_template('home.html', main=main(inp), inp=inp)

if __name__ == '__main__':
    app.run()
