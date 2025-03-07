import os
from dotenv import load_dotenv

#환경 변수 로드
load_dotenv()

#홈페이지에서 API서비스 신청시 받은 Appkey, Appsecret 값 설정
APP_KEY = os.getenv("APP_KEY")
APP_SECRET= os.getenv("APP_SECRET")

MO_APP_KEY= os.getenv("MO_APP_KEY")
MO_APP_SECRET=os.getenv("MO_APP_SECRET")

#계좌번호 앞 8자리
CANO= os.getenv("CANO")
#계좌번호 뒤 2자리
ACNT_PRDT_CD=os.getenv("ACNT_PRDT_CD")

#실전투자
URL_BASE= os.getenv("URL_BASE")
#모의투자
# URL_BASE= os.getenv("APP_KEY")

#디스코드 웹훅 URL
DISCORD_WEBHOOK_URL= os.getenv("DISCORD_WEBHOOK_URL")