from web3 import Web3
from web3.exceptions import TransactionNotFound, TimeExhausted
from dotenv import load_dotenv
import os
import json

def widthDrawUSD(type_token,address_token,monto,to):
    """load_dotenv()
    my_address = os.getenv('ADDRESS')
    private_key = os.getenv('PRIVATE_KEY')
    # Conectar a Celo Mainnet
    w3 = Web3(Web3.HTTPProvider('https://forno.celo.org'))
    # Verificar conexión
    assert w3.is_connected(), "No se pudo conectar a la red Celo"

    # Dirección del Lending Pool (Aave V3 Celo)
    lending_pool_address = '0x3E59A31363E2ad014dcbc521c4a0d5757d9f3402'

    # Dirección del token cUSD
    if(type_token == "USDC"):
        rc20_address = '0xcebA9300f2b948710d2653dD7B07f33A8B32118C'
    elif(type_token == "CUSD"):
        rc20_address = '0x765DE816845861e75A25fCA122bb6898B8B1282a'

    # ABI mínimo para approve
    erc20_abi = json.loads('[{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"type":"function"}]')

    # ABI para supply
    lending_pool_abi = json.loads('[{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"onBehalfOf","type":"address"},{"internalType":"uint16","name":"referralCode","type":"uint16"}],"name":"supply","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

    # Instanciar contratos
    cusd_contract = w3.eth.contract(address=rc20_address, abi=erc20_abi)
    lending_pool = w3.eth.contract(address=lending_pool_address, abi=lending_pool_abi)"""
    return "Hola"

    

    
    

