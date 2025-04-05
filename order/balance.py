## order/balance.py (잔고 조회)

import requests
from config.settings import APP_KEY, APP_SECRET, URL_BASE, ACNT_PRDT_CD

def get_balance():
    """ 한국투자증권 API를 이용해 계좌 잔고 조회 """
    url = f"{URL_BASE}/uapi/domestic-stock/v1/trading/inquire-balance"
    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {APP_KEY}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC8434R"
    }
    params = {"CANO": ACNT_PRDT_CD, "ACNT_PRDT_CD": ACNT_PRDT_CD, "AFHR_FLPR_YN": "N"}

    response = requests.get(url, headers=headers, params=params)
    return response.json()