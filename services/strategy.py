from services.buy_sell import buy, sell
from utils.utils import get_current_price, get_target_price

def execute_buy_strategy(symbol_list, target_buy_count, buy_percent, total_cash, bought_list, access_token):
    buy_amount = total_cash * buy_percent  # 종목별 주문 금액 계산
    for sym in symbol_list:
        if len(bought_list) < target_buy_count:
            if sym in bought_list:
                continue
            target_price = get_target_price(access_token, sym)
            current_price = get_current_price(access_token, sym)
            if target_price < current_price:
                buy_qty = int(buy_amount // current_price)
                if buy_qty > 0:
                    result = buy(sym, buy_qty, access_token)
                    if result:
                        bought_list.append(sym)

def execute_sell_strategy(stock_dict, access_token):
    for sym, qty in stock_dict.items():
        sell(sym, qty, access_token)
