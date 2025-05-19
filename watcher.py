from apscheduler.schedulers.background import BackgroundScheduler
from web3 import Web3
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

def iniciar_watcher():
    scheduler = BackgroundScheduler()
    scheduler.add_job(consultar_bloque, 'interval', minutes=1)
    scheduler.start()
    consultar_bloque()  # Ejecuta al iniciar

def get_ultimo_estado():
    return estado
