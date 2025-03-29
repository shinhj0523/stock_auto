from services.strategy import execute_buy_strategy, execute_sell_strategy
from services.balance import get_balance, get_stock_balance
from utils.utils import send_message
from core.auth import get_access_token
import time
def main():
    send_message("===주식 자동매매 프로그램 시작===")
    access_token = get_access_token()
    symbol_list = ["005930", "035720", "000660", "069500"]  # 매수 희망 종목 리스트
    bought_list = []  # 매수 완료된 종목 리스트
    total_cash = get_balance(access_token)  # 보유 현금 조회
    stock_dict = get_stock_balance(access_token)  # 보유 주식 조회
    
    # # 프로그램 반복 시작
    # while True:
    #     # 전략 실행 예시
    #     execute_buy_strategy(symbol_list, 3, 0.33, total_cash, bought_list, access_token)
    #     execute_sell_strategy(stock_dict, access_token)
    #     time.sleep(1)

def main():
    """자동 매매 시스템 실행"""
    print("자동 매매 시스템 시작")
    
    # 1. 실시간 데이터 수집
    market_data = fetch_market_data()
    
    # 2. VI 발생 종목 필터링
    vi_stocks = filter_vi_stocks()
    selected_stocks = select_top_stocks(vi_stocks)
    
    # 3. 매수 전략 실행
    for stock in selected_stocks:
        if check_buy_signal(stock):
            place_order(stock, quantity=10, order_type="buy")
    
    # 4. 리스크 관리 수행
    manage_risk()
if __name__ == "__main__":
    main()
