from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator", static_folder="static", template_folder="templates")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    textFrench = english_to_french(textToTranslate)
    return textFrench

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    textEnglish = french_to_english(textToTranslate)
    return textEnglish

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
