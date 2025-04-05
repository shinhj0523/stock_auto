## main.py (메인 실행 파일)

from data.fetcher import fetch_market_data, fetch_stock_info
from data.stock_filter import filter_vi_stocks, select_top_stocks
from strategy.entry import check_buy_signal, get_buy_price
from strategy.exit import check_sell_signal
from strategy.risk_management import manage_risk
from order.executor import place_order
from order.balance import get_balance
from utils.notifier import send_discord_alert

def main():
    """자동 매매 시스템 실행"""
    print("🚀 자동 매매 시스템 시작")

    # 1. 실시간 시장 데이터 수집
    market_data = fetch_market_data()

    # 2. VI 발생 종목 필터링
    vi_stocks = filter_vi_stocks(market_data)
    selected_stocks = select_top_stocks(vi_stocks)

    # 3. 매수 전략 실행
    for stock in selected_stocks:
        stock_info = fetch_stock_info(stock["code"])
        buy_price = get_buy_price(stock_info)  # 매수 타점 계산

        if check_buy_signal(stock_info):
            place_order(stock["code"], quantity=10, order_type="buy", price=buy_price)
            send_discord_alert(f"✅ 매수 주문 실행: {stock['code']} / 가격: {buy_price}")

    # 4. 보유 종목에 대한 매도 전략 실행
    balance = get_balance()
    for stock_code in balance["stocks"].keys():
        stock_info = fetch_stock_info(stock_code)

        if check_sell_signal(stock_info):
            place_order(stock_code, quantity=balance["stocks"][stock_code], order_type="sell")
            send_discord_alert(f"🚨 매도 주문 실행: {stock_code}")

    # 5. 리스크 관리 수행
    manage_risk()