# utils/indicators.py

import pandas as pd

def calculate_moving_average(prices: pd.Series, period: int) -> pd.Series:
    """단순 이동 평균선 계산"""
    return prices.rolling(window=period).mean()

def calculate_rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    """RSI (상대강도지수) 계산"""
    delta = prices.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(prices: pd.Series, short_period: int = 12, long_period: int = 26, signal_period: int = 9):
    """MACD 및 시그널 계산"""
    short_ema = prices.ewm(span=short_period, adjust=False).mean()
    long_ema = prices.ewm(span=long_period, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    return macd, signal

def calculate_envelope(prices: pd.Series, period: int, rate: float):
    """
    엔벨로프 밴드 계산
    - 중심선: 이동평균선
    - 상단 밴드: 중심선 * (1 + rate)
    - 하단 밴드: 중심선 * (1 - rate)
    """
    ma = calculate_moving_average(prices, period)
    upper = ma * (1 + rate)
    lower = ma * (1 - rate)
    return upper, lower
