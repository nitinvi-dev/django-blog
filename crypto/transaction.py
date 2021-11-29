import requests
import base58
import base64

from project.settings import METHOD_BALANCE_OF, API_URL_BASE, ADDRESS, CONTRACT, TRANSACTION_URL


def address_to_parameter(addr):
    return "0" * 24 + base58.b58decode_check(addr)[1:].hex()

#
# Trongrid get total balance
#
def trongrid_balance(address=ADDRESS):
    url = '%swallet/triggerconstantcontract' % API_URL_BASE
    payload = {
        'owner_address': base58.b58decode_check(ADDRESS).hex(),
        'contract_address': base58.b58decode_check(CONTRACT).hex(),
        'function_selector': METHOD_BALANCE_OF,
        'parameter': address_to_parameter(address),
    }
    resp = requests.post(url, json=payload)
    data = resp.json()
    try:
        if data['result'].get('result', None):
            val = data['constant_result'][0]
            return int(val, 16)
        else:
            print('error:', bytes.fromhex(data['result']['message']).decode())
            return 0
    except Exception as e:
        return 0


def get_transactions():
    total_in = 0
    in_res = requests.get(TRANSACTION_URL % ("true", "false")).json()
    for amount in in_res["data"]:
        total_in += amount["raw_data"]["contract"][0]["parameter"]["value"]["amount"]

    total_out = 0
    out_res = requests.get(TRANSACTION_URL % ("false", "true")).json()
    for amount in out_res["data"]:
        total_out += amount["raw_data"]["contract"][0]["parameter"]["value"]["amount"]

    return total_in, total_out
