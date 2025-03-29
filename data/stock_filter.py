## data/stock_filter.py (VI 발생 종목 필터링)

def filter_vi_stocks():
    """ VI 발생 종목 중 대장주 필터링 """
    market_data = fetch_market_data()
    return [stock for stock in market_data if stock["vi_triggered"]]

def select_top_stocks(vi_stocks):
    """ 필터링된 종목 중 거래량, 변동성 기준으로 최적 종목 선택 """
    return sorted(vi_stocks, key=lambda x: x["volume"], reverse=True)[:5]

## strategy/entry.py (매수 전략)
from utils.indicators import calculate_rsi