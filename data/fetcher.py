## data/fetcher.py (시세 데이터 수집)
import requests
from config import API_KEY

def fetch_market_data():
    """ 한국투자증권 API를 이용해 실시간 시세 데이터 수집 """
    url = "https://api.yourbroker.com/market_data"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()

def fetch_stock_info(stock_code: str):
    """ 특정 종목의 실시간 정보 조회 """
    url = f"https://api.yourbroker.com/stock/{stock_code}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()