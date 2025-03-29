## order/executor.py (주문 실행)

def place_order(stock_code: str, quantity: int, order_type: str):
    """ 매수 및 매도 주문 실행 """
    print(f"{order_type.upper()} 주문 실행: {stock_code}, 수량: {quantity}")