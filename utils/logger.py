## utils/logger.py (로그 관리)

def log_message(message: str):
    """ 시스템 실행 로그 저장 """
    with open("log.txt", "a") as log_file:
        log_file.write(f"{message}\n")