Kill Fps game Cheater (KFC)

KFC는 오버워치 불법 프로그램 사용자를 잡아주는 프로그램입니다.

오픈소스인 yolo를 기반으로 오버워치 영웅들을 인식하고, linear regression을 이용하여 불법 프로그램 사용 여부를 판단해줍니다.

약 25000장을 labelling하여 데이터를 생성하였고 약 5만번 정도의 training이 된 weight파일을 사용합니다.

KFC의 알고리즘은 다음과 같습니다.

1. 동영상 파일이 삽입되면, 우선 동영상을 프레임단위로 자른다.
2. 프레임마다 weights파일을 이용해 YOLO를 매칭시켜, 영웅이 존재하는지, death-sign이 존재하는지 detect한다
3. 만약 death-sign이 발견되면 그 전의 10프레임을 확인해, 각 프레임마다 영웅과 aim 사이의 거리를 추출한다.
4. 이전프레임과의 거리의 차 10개를 선형 머신에 넣고 돌려, 보통범위 내의 값인지, 아니면 이상이 있는 값인지를 확인한다.
5. 이상이 있을 경우 hack임을 , 이상이 없을 경우 normal user임을 output으로 알려준다.

![image](https://user-images.githubusercontent.com/45477589/102713470-d4462480-430b-11eb-9c63-3a4f5311ebef.png)

main-> getframe -> get feature -> distance -> machine learning
추가적으로 이해를 도울 sequence diagram을 첨부했습니다.

test를 위한 동영상과 weights파일은 원드라이브에 있어, 링크를 첨부했습니다.

이하는 설치 및 구동 매뉴얼입니다. 프로젝트를 사용해 보고 싶으시다면 읽고 따라해보세요.
