# 자막 메이커 프로젝트  
*2018년도 데이터베이스 수업 과제*  
<br><br><br>
## 서비스의 목적과 배경  
 우리는 유튜브를 통해서 전세계의 여러 다양한 창작물들을 만날 수 있습니다.  
 유튜브에서는 자동 번역 기능을 제공해주며 세계인들간의 언어 장벽을 허물어주고 있습니다.  
<br>
 여기서 한가지 재밌는 생각이 떠올랐습니다.  
 구글 번역기보다, 파파고 번역기를 자주쓰는 1인.  
 __"구글 말고 파파고가 유튜브 영상을 자동 번역하면 어떨까?"__
 <br><br>
 ## 활용한 공공 데이터  
- __IBM Watson Speech to Text API, 네이버 papago API__  
  - __IBM 선택 이유?__ <br> 구글 stt도 써보고 싶었는데, 제작 방향이 구글 번역에 대항하는 프로그램을 만드는 것이라서 경쟁사인 IBM을 선택했다.<br>또한, IBM은 AI 개발에 있어서 오랫동안 투자해 온 기업이라 믿음이 갔다.  
  - __추가 정보__ :  https://www.ibm.com/kr-ko/cloud/watson-speech-to-text
<br><br><br>
## 주요 기능  
__| IBM Watson Sppech To Text |__
- Speech To Text 시작하기 : https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-gettingStarted&locale=ko  
  - Speech To Text  
<br><br><br>
__| Naver papago API |__  
- papago 구현 예제 : https://developers.naver.com/docs/papago/papago-nmt-example-code.md  
- papago API 레퍼런스 : https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-gettingStarted&locale=ko  
  - 번역할 음성파일의 언어 감지  
  - 파파고 인공지능 번역  

## 동작 시나리오  
1. 단순 번역  

2. 음성 파일 번역
