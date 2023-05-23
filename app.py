from flask import Flask,render_template,request
import requests

headers= {
  "apikey": "vQzy4Q3cRmdvbzalGZwn4MjP4Pczym4S"
}

# made by me github desktop

app = Flask(__name__)

@app.route("/" , methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency") # EURO
        secondCurrency = request.form.get("secondCurrency") # TRY
        amount = request.form.get("amount") #20
        url = "https://api.apilayer.com/fixer/convert?to="+secondCurrency+"&from="+firstCurrency+"&amount="+amount
        currencyInfo = dict()
        response = requests.request("GET", url, headers=headers, data = currencyInfo)
        #app.logger.info(response)
        infos = response.json()
        firstValue = infos["query"]["from"]
        secondValue = infos["query"]["to"]
        result = infos["result"]
        
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result
        #app.logger.info(infos)
        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")









if __name__ == "__main__":
    app.run(debug = True)
