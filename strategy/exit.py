## strategy/exit.py (매도 전략)

def check_sell_signal(stock_code: str):
    """ 손절 및 익절 조건 체크 """
    stock_data = fetch_stock_info(stock_code)
    rsi = calculate_rsi(pd.Series(stock_data["close_prices"]))
    return rsi.iloc[-1] > 70