## data/stock_filter.py (VI 발생 종목 필터링)
import pandas as pd

def filter_vi_stocks(market_data):
    """ 
    📌 VI(변동성 완화 장치) 발동 종목 필터링  
    - VI 발동 조건: 시초가 대비 10% 이상 상승한 종목 탐색
    - 거래 정지 동안 종목을 모니터링하여 적절한 진입 기회 탐색
    """
    vi_stocks = []
    for stock in market_data:
        # VI 발동 여부 확인 (시초가 대비 10% 상승)
        if stock["current_price"] >= stock["open_price"] * 1.1:
            vi_stocks.append(stock)
    return vi_stocks

def select_top_stocks(vi_stocks):
    """
    📌 VI 발동 종목 중 대장주 선정  
    - 거래량 기준으로 상위 종목 선정
    - 이동평균선(5일선 & 10일선) 골든크로스 발생 여부 확인
    - 전일 대비 거래량 증가율 400% 이상인지 필터링
    """
    if not vi_stocks:
        return []

    # 거래량 기준 정렬하여 대장주 찾기
    sorted_stocks = sorted(vi_stocks, key=lambda x: x["volume"], reverse=True)

    # 이동평균선 골든크로스 및 거래량 증가율 400% 체크
    filtered_stocks = []
    for stock in sorted_stocks:
        if stock["golden_cross"] and stock["volume_increase"] >= 400:
            filtered_stocks.append(stock)

    return filtered_stocks[:5]  # 최종적으로 상위 5개 종목 선택
