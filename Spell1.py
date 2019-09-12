import flask,re
from flask import request
from autocorrect import spell
from pattern.en import suggest

app = flask.Flask(__name__)
app.config["DEBUG"] = True



def reduce_lengthening(text):
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", text)

#@app.route('/sp/<string:given_word>', methods=['GET'])
@app.route('/spellCorrect', methods=['GET'])
def f():
    given_word = request.args.get('word')    ### get paramter
    
    
    given_word = given_word.encode('ascii', 'ignore').decode('ascii') ### removing emojis 
    
    given_word=re.sub('[^A-Za-z0-9]+', '', given_word)##removing special characters
    
    given_word=''.join([i for i in given_word if not i.isdigit()]) ##removing numerics
    
    given_word=given_word.replace(" ", "")###remove all type of white spaces
    
    reduced_word = reduce_lengthening(given_word) #####removing repeated characters
    
    
    
    return spell(reduced_word)
    #return suggest(reduced_word)
    #return reduced_word
    
    
       


#       word_without_emoji = deEmojify(given_word)

#       word_without_space = word_without_emoji .replace(" ", "")

#       reduced_word = reduce_lengthening(given_word)

app.run()
