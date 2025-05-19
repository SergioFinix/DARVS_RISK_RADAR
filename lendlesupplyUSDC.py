from web3 import Web3
from web3.exceptions import TransactionNotFound, TimeExhausted
from dotenv import load_dotenv
import os
import json

def lendle_supply_usdc():
    # Cargar variables de entorno
    load_dotenv()
    my_address = os.getenv('ADDRESS')
    private_key = os.getenv('PRIVATE_KEY')

    # Conexión a Mantle Mainnet
    w3 = Web3(Web3.HTTPProvider('https://rpc.mantle.xyz'))
    assert w3.is_connected(), "No se pudo conectar a Mantle"

    # Dirección del contrato de USDC y LendingPool (Lendle)
    usdc_address = Web3.to_checksum_address('0x09BC4E0D864854C6aFB6Eb9a9CDF58ac190d0Df9')  # USDC (Mantle)
    lending_pool_address = Web3.to_checksum_address('0xCFa5aE7c2CE8Fadc6426C1ff872cA45378Fb7cF3')  # Lendle LendingPool

    # ABIs mínimos
    erc20_abi = json.loads('''
    [
      {
        "constant": false,
        "inputs": [{"name": "spender", "type": "address"}, {"name": "amount", "type": "uint256"}],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
      },
      {
        "constant": true,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
      },
      {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
      }
    ]
    ''')

    lending_pool_abi = json.loads('''
    [
      {
        "inputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "onBehalfOf",
                "type": "address"
            },
            {
                "internalType": "uint16",
                "name": "referralCode",
                "type": "uint16"
            }
        ],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
    ]
    ''')

    # Instanciar contratos
    usdc = w3.eth.contract(address=usdc_address, abi=erc20_abi)
    lending_pool = w3.eth.contract(address=lending_pool_address, abi=lending_pool_abi)

    # Obtener decimales del token
    decimals = usdc.functions.decimals().call()
    print("Decimales del token:", decimals)

    # Monto a depositar: 1 USDC
    amount = 1 * (10 ** decimals)
    print("Monto en wei:", amount)

    # Paso 1: Approve
    nonce = w3.eth.get_transaction_count(my_address)
    gas_price = w3.eth.gas_price
    print("Presion del Gas : -----",gas_price)
    approve_tx = usdc.functions.approve(lending_pool_address, amount).build_transaction({
        'from': my_address,
        'nonce': nonce,
        'gas': 2807,
        'gasPrice': gas_price,
        
    })
    
    # Estimar gas para approve
    print(approve_tx)
    print("++++++++")
    gas_estimado = w3.eth.estimate_gas(approve_tx)
    print("*******************++++")
    approve_tx['gas'] = gas_estimado
    print("Gas estimado para approve:", gas_estimado)

    signed_approve = w3.eth.account.sign_transaction(approve_tx, private_key)
    tx_hash_approve = w3.eth.send_raw_transaction(signed_approve.raw_transaction)
    print("Approve tx hash:", tx_hash_approve.hex())
    w3.eth.wait_for_transaction_receipt(tx_hash_approve ,timeout=180)
    print("Approve confirmado")

    # Paso 2: Supply
    nonce += 1
    
    supply_tx = lending_pool.functions.deposit(usdc_address, amount, my_address, 0).build_transaction({
        'from': my_address,
        'nonce': nonce,
        'gasPrice': gas_price,
    })

    print(supply_tx)
    

    signed_supply = w3.eth.account.sign_transaction(supply_tx, private_key)
    tx_hash_supply = w3.eth.send_raw_transaction(signed_supply.raw_transaction)
    print("Supply tx hash:", tx_hash_supply.hex())
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash_supply,timeout=180)
    print("Supply confirmado:", receipt.transactionHash.hex())

    return "Supply exitoso"

def getHealtFactor(user_address):
    # Conexión a Mantle Mainnet
    w3 = Web3(Web3.HTTPProvider('https://rpc.mantle.xyz'))
    assert w3.is_connected(), "No se pudo conectar a Mantle"

    addreUser = Web3.to_checksum_address(user_address)  # Lendle LendingPool
    contract_address     = Web3.to_checksum_address('0xCFa5aE7c2CE8Fadc6426C1ff872cA45378Fb7cF3')  # Lendle LendingPool
    infoUser_pool_abi = json.loads('''
    [
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "user",
                    "type": "address"
                }
            ],
            "name": "getUserAccountData",
            "outputs": [
                { "internalType": "uint256", "name": "totalCollateralETH", "type": "uint256" },
                { "internalType": "uint256", "name": "totalDebtETH", "type": "uint256" },
                { "internalType": "uint256", "name": "availableBorrowsETH", "type": "uint256" },
                { "internalType": "uint256", "name": "currentLiquidationThreshold", "type": "uint256" },
                { "internalType": "uint256", "name": "ltv", "type": "uint256" },
                { "internalType": "uint256", "name": "healthFactor", "type": "uint256" }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]
                                   ''')
    # Crear la instancia del contrato
    contract = w3.eth.contract(address=contract_address, abi=infoUser_pool_abi)
    user_address = Web3.to_checksum_address(addreUser)

    # Llamar a la función
    data = contract.functions.getUserAccountData(user_address).call()

    # Imprimir los resultados
    (
        totalCollateralETH,
        totalDebtETH,
        availableBorrowsETH,
        currentLiquidationThreshold,
        ltv,
        healthFactor
    ) = data

    #print("Total Collateral (ETH):", Web3.from_wei(totalCollateralETH, 'ether'))
    #print("Total Debt (ETH):", Web3.from_wei(totalDebtETH, 'ether'))
    #print("Available Borrows (ETH):", Web3.from_wei(availableBorrowsETH, 'ether'))
    #print("Current Liquidation Threshold:", currentLiquidationThreshold)
    #print("LTV:", ltv)
    #print("Health Factor:", healthFactor / (10 ** 18))  # Normalmente healthFactor está en 18 decimales

    return healthFactor / (10 ** 18)