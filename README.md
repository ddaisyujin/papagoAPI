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
- 다양한 언어 ver : https://cloud.ibm.com/apidocs/speech-to-text?code=python
  - Speech To Text  

<br><br><br>
__| Naver papago API |__  
- papago 구현 예제 : https://developers.naver.com/docs/papago/papago-nmt-example-code.md  
- papago API 레퍼런스 : https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-gettingStarted&locale=ko  
  - 번역할 음성파일의 언어 감지  
  - 파파고 인공 신경망 기반의 기계 번역(NMT, Neural Machine Translation)
<br><br><br><br><br><br>
## 동작 시나리오  
__1. 단순 번역__
<br><br>
![image](https://user-images.githubusercontent.com/35206992/103107508-532bbc00-4682-11eb-81ba-ae4380e87f4b.png)
<br><br><br>
![image](https://user-images.githubusercontent.com/35206992/103107524-722a4e00-4682-11eb-9c94-9101365bcd2a.png)
<br><br><br><br><br><br>
|*참고*|  
![image](https://user-images.githubusercontent.com/35206992/103107874-fc27e600-4685-11eb-9a4a-149cc26c3493.png)
<br><br><br><br><br><br>
<br><br><br><br><br><br>
__2. 음성 파일 번역__
<br><br>
![image](https://user-images.githubusercontent.com/35206992/103107535-94bc6700-4682-11eb-8132-9043cd04bc9d.png)
<br><br><br>
![image](https://user-images.githubusercontent.com/35206992/103107553-d2b98b00-4682-11eb-8a87-8fa99c8f4914.png)
<br><br><br>
![image](https://user-images.githubusercontent.com/35206992/103107597-625f3980-4683-11eb-815a-038571f31f27.png)
<br><br><br><br><br><br>

## 정리겸 잡담  
실험 결과, 파파고와 구글 중 누가 더 뛰어난지 "아직은" 결정하긴 힘듦.  
*내눈엔 둘 다 비슷해 보인다.*  
번역한 결과를 그대로 복사 붙여넣기해도 이상하지않을 만큼 자연스러워졌지만,<br>
여전히 번역체가 남아있긴하다.  
<br><br>
영어를 띄어쓰기하지 않았을 때, 영어 문법을 잘 맞추는 것은 구글!  
영어가 제대로 쓰였을 때, 한국 스타일에 맞게 번역하는 것은 파파고!  
<br><br><br><br><br>
