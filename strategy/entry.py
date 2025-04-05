## strategy/entry.py (매수 전략)

import pandas as pd
from utils.indicators import calculate_rsi, calculate_macd, calculate_envelope

def get_buy_price(stock_info):
    """ 
    📌 매수 타점 결정 (VI 가격, 이동평균선, 엔벨로프, RSI, MACD 고려)  
    - 1차 매수: VI 발동 가격에서 매수  
    - 2차 매수: 60틱 차트 60이평선 & 120이평선 도달 시 매수  
    - 3차 매수: 120이평선 -3% 엔벨로프 하단  
    - 4차 매수: 120이평선 -5% 엔벨로프 하단  
    - 5차 매수: RSI 과매도 (30 이하) 진입 시 매수  
    - 6차 매수: MACD 골든크로스 발생 시 매수  
    """
    price = stock_info["vi_price"]  # 기본적으로 VI 가격에서 매수

    # 120이평선 -3% 지점 체크
    envelope_3 = calculate_envelope(stock_info["moving_avg_120"], -3)
    if stock_info["current_price"] <= envelope_3:
        return envelope_3

    # 120이평선 -5% 지점 체크
    envelope_5 = calculate_envelope(stock_info["moving_avg_120"], -5)
    if stock_info["current_price"] <= envelope_5:
        return envelope_5

    return price  # 기본적으로 VI 가격에서 매수

def check_buy_signal(stock_info):
    """ 
    📌 매수 신호 판단 (RSI, MACD 활용)  
    - RSI 30 이하: 과매도 구간에서 매수  
    - MACD 골든크로스 발생 시 매수 신호 감지  
    """
    if stock_info["rsi"] < 30:
        return True  # RSI 과매도 진입 시 매수

    macd, signal = calculate_macd(pd.Series(stock_info["close_prices"]))
    if macd.iloc[-1] > signal.iloc[-1]:  # MACD 골든크로스 발생
        return True

    return False
