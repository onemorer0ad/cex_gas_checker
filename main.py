import config
import ccxt


TOKEN = 'TON'  # Enter token => 'ETH', 'BNB', 'AVAX', 'USDC', 'USDT', etc.
NETWORK = 'TON'  # Enter network => 'Arbitrum one', 'Polygon', 'ERC20', 'zkSync Lite', 'Optimism', 'BSC', 'TRC20', 'Avalanche C-Chain', etc.



def okx_get_fee(token, network):
    try:
        exchange = ccxt.okx({
            'apiKey': config.okx_apikey,
            'secret': config.okx_apisecret,
            'password': config.okx_passphrase,
            'enableRateLimit': True,
        })
        info = exchange.fetch_currencies()
        network_fee = info[token]['networks'][network]['fee']
        return network_fee
    except Exception as e:
        print(f'okx_get_fee error: {e}')

def binance_get_fee(token, network):
    try:
        exchange = ccxt.binance({
            'apiKey': config.binance_apikey,
            'secret': config.binance_apisecret,
            'enableRateLimit': True,
        })
        info = exchange.fetch_currencies()
        network_fee = info[token]['networks'][network]['fee']
        return network_fee
    except Exception as e:
        print(f'binance_get_fee error: {e}')

def bybit_get_fee(token, network):
    try:
        exchange = ccxt.bybit({
            'apiKey': config.bybit_apikey,
            'secret': config.bybit_apisecret,
            'enableRateLimit': True,
        })
        info = exchange.fetch_currencies()
        network_fee = info[token]['networks'][network]['fee']
        return network_fee
    except Exception as e:
        print(e)

def bitget_get_fee(token, network):
    try:
        exchange = ccxt.bitget({
            'apiKey': config.bitget_apikey,
            'secret': config.bitget_apisecret,
            'enableRateLimit': True,
        })
        info = exchange.fetch_currencies()
        network_fee = info[token]['networks'][network]['fee']
        return network_fee
    except Exception as e:
        print(f'bitget_get_fee error: {e}')

def mexc_get_fee(token, network):
    try:
        exchange = ccxt.mexc({
            'apiKey': config.mexc_apikey,
            'secret': config.mexc_apisecret,
            'enableRateLimit': True,
        })
        info = exchange.fetch_currencies()
        network_fee = info[token]['networks'][network]['fee']
        return network_fee
    except Exception as e:
        print(f'mexc_get_fee error: {e}')


if __name__ == '__main__':
    fees = {
        'binance': binance_get_fee(TOKEN, NETWORK),
        'okx': okx_get_fee(TOKEN, NETWORK),
        'bybit': bybit_get_fee(TOKEN, NETWORK),
        'bitget': bitget_get_fee(TOKEN, NETWORK),
        'mexc': mexc_get_fee(TOKEN, NETWORK),
    }

    for exchange, fee in fees.items():
        print(f'{exchange} fee: {fee} {NETWORK}')
