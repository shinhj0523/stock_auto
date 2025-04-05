## data/fetcher.py (시세 데이터 수집)
import requests
from config.settings import APP_KEY, APP_SECRET, URL_BASE

def fetch_market_data(stock_code):
    """ 한국투자증권 API를 이용해 실시간 시세 데이터 조회 """
    url = f"{URL_BASE}/uapi/domestic-stock/v1/quotations/inquire-price"
    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {APP_KEY}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "FHKST01010100"  # 실시간 시세 조회 API 거래 ID
    }
    params = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": stock_code}
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def fetch_stock_info(stock_code: str):
    """ 특정 종목의 실시간 정보 조회 """
    url = f"https://api.yourbroker.com/stock/{stock_code}"
    headers = {"Authorization": f"Bearer {APP_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()