"""
pydoor python program

this program uses python flask to host the sign on my door
"""

from flask import Flask, render_template, request
import json
from os import listdir
from os.path import isfile, join

#enable personal debug messages
DEBUG = True

try:
    with open("cards.json") as f:
        cardsdict = json.load(f)
except:
    cardsdict = []
    
try:
    with open("messages.json") as f:
        messagesdict = json.load(f)
except:
    messagesdict = []

app = Flask(__name__, template_folder='html/templates/')

@app.route('/')
def index() :
    cardnum = request.args.get('card')
    
    if DEBUG:
        print("DEBUG: cardnum = ", cardnum)
        print("DEBUG: cardnum type = ", type(cardnum))
        
    
    if str(cardnum) == str("None"):
        return render_template('pleasescan.html',)
    
    try:
        if cardsdict[cardnum]['active'] == 'A':
            cardsdict[cardnum]['active'] = 'B'
            return render_template(messagesdict[cardsdict[cardnum]['B']]['template'], **messagesdict[cardsdict[cardnum]['B']])    
        elif cardsdict[cardnum][active] == 'B':
            cardsdict[cardnum][active] = 'A'
            return render_template(cardsdict[cardnum]['A'],)
    except:
        return render_template('cardnotfound.html',)
    
@app.route('/edit')
def edit() :
    mypath = "html/templates/"
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    files.remove("base.html")
    files.remove('template.html')
    
    if DEBUG:
        print(files)
        
    return str(files)

if __name__ == '__main__' :
    # WARNING FLASK IS IN DEBUG MODE DISABLE FOR PRODUCTION SERVER
    app.run(debug=True, host='::', port=80)
