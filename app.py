from flask import Flask, jsonify
from watcher import iniciar_watcher, get_ultimo_estado
from supplycUSD import supplyCusd
from lendlesupplyUSDC import lendle_supply_usdc,getHealtFactor
from widthDrawAave import widthDrawUSD

app = Flask(__name__)
iniciar_watcher()  # Inicia el scheduler

@app.route('/')
def index():
    return "HealthWatcher corriendo!"

@app.route('/getHealtFactor/<string:userWallet>', methods=['GET'])
def getHealtFactorUser(userWallet):
    return jsonify(getHealtFactor(userWallet))

@app.route('/estado', methods=['GET'])
def estado():
    return jsonify(get_ultimo_estado())

@app.route('/supplyCusd/<string:type_token>', methods=["GET"])
def supplyCusdm(type_token):
    return jsonify(supplyCusd(type_token))

@app.route('/lendeSupplyUsdc', methods=["GET"])
def supplyLendleUsdc():
    return jsonify(lendle_supply_usdc())

@app.route('/<string:type_token>/widthdraw/<string:address_token>/<string:monto>/<string:to>', methods=["GET"])
def widthdrawPostionm(type_token,address_token,monto,to):
    return jsonify(widthDrawUSD(type_token,address_token,monto,to))

if __name__ == '__main__':
    app.run(debug=True)
