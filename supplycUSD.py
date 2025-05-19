from web3 import Web3
from web3.exceptions import TransactionNotFound, TimeExhausted
from dotenv import load_dotenv
import os
import json

def supplyCusd(type_token):
    # Cargar variables desde .env
    load_dotenv()
    my_address = os.getenv('ADDRESS')
    private_key = os.getenv('PRIVATE_KEY')

    # Conectar a Celo Mainnet
    w3 = Web3(Web3.HTTPProvider('https://forno.celo.org'))

    # Verificar conexión
    assert w3.is_connected(), "No se pudo conectar a la red Celo"

    # Dirección del Lending Pool (Aave V3 Celo)
    lending_pool_address = '0x3E59A31363E2ad014dcbc521c4a0d5757d9f3402'

    #usdc contract
    #0xcebA9300f2b948710d2653dD7B07f33A8B32118C
    #cusdc contract
    #0x765DE816845861e75A25fCA122bb6898B8B1282a
    
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
    lending_pool = w3.eth.contract(address=lending_pool_address, abi=lending_pool_abi)

    # Cantidad a depositar: 10 cUSD
    amount = w3.to_wei(1.2, 'ether')
    print ("monto : ", amount)

    if(type_token == "USDC"):
        print("entra en conversion")
        amount = int(amount / 1000000000000)
        print ("monto 2 : ", amount)    

    # Paso 1: Approve
    nonce = w3.eth.get_transaction_count(my_address)

    gas_price = w3.eth.gas_price
    print("Precio del gas 1 : ",gas_price )
    gas_limit = 300000 

    approve_tx = cusd_contract.functions.approve(lending_pool_address, amount).build_transaction({
        'from': my_address,
        'nonce': nonce,
        'gas': gas_limit,
        'gasPrice': gas_price,
    })

    gasEstimacion1 = w3.eth.estimate_gas(approve_tx)
    print("Estimación gas 1",gasEstimacion1)

    signed_approve = w3.eth.account.sign_transaction(approve_tx, private_key)

    # Verificación del tipo de signed_approve para asegurarnos de que tiene rawTransaction
    #print("Tipo de signed_approve:", type(signed_approve))
    #print("Métodos de signed_approve:", dir(signed_approve))

    # Comprobar si rawTransaction existe en signed_approve
    #if hasattr(signed_approve, 'raw_transaction'):
    approve_hash = w3.eth.send_raw_transaction(signed_approve.raw_transaction)
    #print('Approve sent:', approve_hash.hex())
    w3.eth.wait_for_transaction_receipt(approve_hash ,timeout=180)
    #else:
        #print("Error: 'rawTransaction' no está presente en signed_approve")

    # Paso 2: Supply
    nonce += 1
    supply_tx = lending_pool.functions.supply(rc20_address,amount,my_address,0).build_transaction({
        'from': my_address,
        'nonce': nonce,
        'gas': gas_limit,
        'gasPrice': gas_price,
    })

    signed_supply = w3.eth.account.sign_transaction(supply_tx, private_key)
    supply_hash = w3.eth.send_raw_transaction(signed_supply.raw_transaction)
    print('Supply sent :', supply_hash.hex())
    receipt = w3.eth.wait_for_transaction_receipt(supply_hash,timeout=180)
    print('Supply confirmed :', receipt)

    return "Supply exitoso"
