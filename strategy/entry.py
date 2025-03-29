## strategy/entry.py (매수 전략)
from utils.indicators import calculate_rsi

def check_buy_signal(stock_code: str):
    """ 오버솔드 기반 매수 신호 감지 """
    stock_data = fetch_stock_info(stock_code)
    rsi = calculate_rsi(pd.Series(stock_data["close_prices"]))
    return rsi.iloc[-1] < 30