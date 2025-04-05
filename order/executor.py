## order/executor.py (주문 실행)

import requests
from config.settings import APP_KEY, APP_SECRET, URL_BASE, ACNT_PRDT_CD

def place_order(stock_code: str, quantity: int, order_type: str):
    """ 한국투자증권 API를 이용해 매수 및 매도 주문 실행 """
    url = f"{URL_BASE}/uapi/domestic-stock/v1/trading/order-cash"
    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {APP_KEY}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC0802U" if order_type == "buy" else "TTTC0801U"
    }
    params = {
        "CANO": ACNT_PRDT_CD,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": stock_code,
        "ORD_QTY": str(quantity),
        "ORD_UNPR": "0",  # 시장가 주문
        "ORD_DVSN": "01",  # 시장가 주문 코드
        "CVDG_ACNT_NO": "",
        "MGCO_APTM_ODNO": ""
    }

    response = requests.post(url, headers=headers, json=params)
    return response.json()
