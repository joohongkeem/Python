print("-------------------------------------------------")
print("# 20180706", "Made by joohongkeem#".rjust(38), sep=' ', end='\n')
print("-------------------------------------------------")

# 로깅(Logging)
# 정의 : 프로그램이 실행될 때 일어나는 이벤트를 추적하기 위한 용도로 소스코드에 삽입하는
#        출력문을 작성하는 것. 결과로 발생하는 출력문을 로그라고 함.

# 로그 레벨: Debug > Info > Warning > Error > Critical (개발자는 주로 Debug 레벨)

import logging

logging.warning('조심!!')
logging.info('정보 확인 요!')  # 출력되지 않음. 파이썬의 기본 로거는 root 이며,
# 로그 레벨은 Warning 이므로 낮은 레벨인 Info, debug는 출력하지 않음
logging.root.setLevel(logging.DEBUG)  # 로그 레벨 변경
logging.info('정보 확인 바람!')  # info 메세지 출력됨

# 로깅 관련 객체
# - Logget : 파이썬 모듈 단위로 로거 생성. 모든 로거는 root 로거의 자식
# - Handler : 로거에 의해 생성된 log record를 적절한 곳에 출력(콘솔, 파일 DB 등). 로거는 여러개의 핸들러 보유
# - Formatter : 로그 출력 포맷 결정

logger = logging.getLogger(__name__)  # 로거 생성
logger.warning('문제가 생길지도 모름')

# 로깅 모듈
import logging

# 콘솔 출력용 핸들러 생성
handler = logging.StreamHandler()

# 포매터 생성
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')

# 핸들러에 포매터 설정
handler.setFormatter(formatter)

# 로거 생성 및 로그 레벨 설정
logger = logging.getLogger(__name__) # 로거 생성
logger.setLevel(logging.INFO) # 로그 레벨설정 : INFO
logger.addHandler(handler) # 해당 로거에 핸들러 추가

# 로그 메세지 출력
logger.debug('이 메세지는 개발자만 이해해요.') # DEBUG 로그 출력
logger.info('생각대로 동작 하고 있어요.') # INFO 로그 출력
logger.warning('워닝이야') # Warning 로그 출력
logger.error('에러다') # Error 로그 출력
logger.critical('노답') # Critical 로그 출력
