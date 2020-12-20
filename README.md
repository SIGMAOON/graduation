# Kill Fps game Cheater (KFC)     
     
KFC는 오버워치 불법 프로그램 사용자를 잡아주는 프로그램입니다.        
오픈소스인 yolo를 기반으로 오버워치 영웅들을 인식하고, linear regression을 이용하여 불법 프로그램 사용 여부를 판단해줍니다.     
약 25000장을 labelling하여 데이터를 생성하였고 약 5만번 정도의 training이 된 weight파일을 사용합니다.     
     
### KFC의 알고리즘은 다음과 같습니다.      
      
1. 동영상 파일이 삽입되면, 우선 동영상을 프레임단위로 자른다.       
2. 프레임마다 weights파일을 이용해 YOLO를 매칭시켜, 영웅이 존재하는지, death-sign이 존재하는지 detect한다    
3. 만약 death-sign이 발견되면 그 전의 10프레임을 확인해, 각 프레임마다 영웅과 aim 사이의 거리를 추출한다.      
4. 이전프레임과의 거리의 차 10개를 선형 머신에 넣고 돌려, 보통범위 내의 값인지, 아니면 이상이 있는 값인지를 확인한다.      
5. 이상이 있을 경우 hack임을 , 이상이 없을 경우 normal user임을 output으로 알려준다.      

main-> getframe -> get feature -> distance -> machine learning     
### 추가적으로 이해를 도울 sequence diagram을 첨부했습니다.     
![image](https://user-images.githubusercontent.com/45477589/102713470-d4462480-430b-11eb-9c63-3a4f5311ebef.png)     
  
### 이하는 설치 및 구동 매뉴얼입니다. 프로젝트를 사용해 보고 싶으시다면 읽고 따라해보세요.    
test를 위한 input용 영상과 weights 파일은 원드라이브에 업로드 해 두었습니다. (6,7번에 링크 첨부)     
      
1. 구글 colaboratory 사이트에 접속합니다.     
> [Google Colab](https://colab.research.google.com/, "google colab link") 
2. 팝업창의 우측 하단에 있는 새 노트를 클릭합니다.     
3. 상단메뉴의 런타임 - 런타임 유형 변경에서 하드웨어 가속기를 GPU로 변경합니다.     
4. graduation 폴더 github로부터 가져옵니다.(git clone 코드를 colab에 입력)       
> !git clone https://github.com/SIGMAOON/graduation.git      
5. 이때 colab의 경로 이동 문제가 발생하므로 graduation 폴더 밖으로 파일들 이동합니다. (mv 코드를 입력)     
> !mv graduation/* ./     
6. video 파일을 다운로드 후 압축을 풀어 data/video/ 경로에 넣습니다.     
> [Video File Download Link](https://hongik-my.sharepoint.com/:u:/g/personal/chiseungii_mail_hongik_ac_kr/EYuiHx2_ondCh70K9z_yLXcB5UJvtRAcDCrDQTFTMgOgJw?e=Y41ydX, "video download link") 
7. weights 파일 다운로드 후 압축 풀어서 weights/ 경로에 넣습니다.       
> [Weights File Download Link](https://hongik-my.sharepoint.com/:u:/g/personal/chiseungii_mail_hongik_ac_kr/EUI8K6izM81Ku42lVxOuEUYB0hpMN0mg8saShrBRMLRgdA?e=XqYzMM, "weights file download link")
8. 프로그램을 실행합니다.(pythoh 실행코드를 입력)       
> !python KFC.py      
9. 영상 이름을 뒤에 확장자까지 입력합니다. (exam_normal.mp4은 정상 유저의 영상, exam_hack.mp4은 불법 프로그램 사용자의 영상)      
> ex) exam_normal.mp4        
10. weights 파일 이름도 뒤에 확장자까지 입력합니다.       
(obj_test_64000.weights은 프로젝트의 알고리즘 실행이 잘 되는 지 확인하기 위해서 test용 input 영상만을 학습한 파일, yolov3_51000.weights은 다양한 영상을 모든 캐릭터에 대하여 학습한 파일)          
> ex) obj_test_64000.weights      
