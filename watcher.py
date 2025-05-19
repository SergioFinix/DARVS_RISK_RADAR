from apscheduler.schedulers.background import BackgroundScheduler
from web3 import Web3
from flask import jsonify
from lendlesupplyUSDC import getHealtFactor
import time

# Puedes poner esto en config.py también
CELO_RPC = "https://rpc.mantle.xyz"
web3 = Web3(Web3.HTTPProvider(CELO_RPC))

estado = {"ultimo_bloque": None, "timestamp": None}

def consultar_bloque():
    try:
        numero_bloque = web3.eth.block_number
        timestamp = int(time.time())
        estado["ultimo_bloque"] = numero_bloque
        estado["timestamp"] = timestamp
        print(f"[Watcher] Bloque actual: {numero_bloque}")
    except Exception as e:
        print(f"[Watcher] Error: {e}")

def getHealtFactorUser():
    userWallet ="0x09BB59c870AA5CB0e7A01b2f96d72B29f3a4BE90"
    return print(f"Healt Factor: {getHealtFactor(userWallet)}")

def iniciar_watcher():
    scheduler = BackgroundScheduler()
    scheduler.add_job(getHealtFactorUser, 'interval', minutes=1)
    scheduler.start()
    getHealtFactorUser()  # Ejecuta al iniciar

def get_ultimo_estado():
    return estado
