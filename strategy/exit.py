## strategy/exit.py (매도 전략)

def check_sell_signal(stock_info):
    """ 
    📌 매도 신호 판단 (손절 & 익절 전략)  
    - 3분봉 5이평선 이탈 시 손절  
    - 60틱 차트 20이평선 & 60이평선 이탈 시 손절  
    - RSI 70 이상 도달 시 익절  
    - 60틱 차트 60이평선 & 120이평선 도달 시 익절  
    """
    if stock_info["rsi"] > 70:
        return True  # RSI 과매수 도달 시 익절

    if stock_info["current_price"] < stock_info["moving_avg_5"]:
        return True  # 3분봉 5이평선 이탈 시 손절

    if stock_info["current_price"] < stock_info["moving_avg_60"]:
        return True  # 60틱 차트 60이평선 이탈 시 손절

    return False
