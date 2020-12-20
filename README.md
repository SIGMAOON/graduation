kfc프로젝트는 오픈소스인 yolo를 기반으로 한 오버워치 게임화면을 이용한 불법프로그램 디텍팅 프로그램입니다. 
약 20000장을 labelling시키고, 약 5만번 정도의 training을 거친 weight파일을 생성해 이용합니다.
1. 동영상 파일이 삽입되면, 우선 동영상을 프레임단위로 자른다.
2. 프레임마다 weight파일과 매칭시켜, 영우이 존재하는지, death-sign이 존재하는지 detect한다
3. 만약 death-sign이 발견되면 그 전의 10프레임을 확인해, 각 프레임마다 영웅과 aim 사이의 거리를 추출한다.
4. 추출한 10개의 거리를 선형 머신에 넣고 돌려, 보통범위 내의 값인지, 아니면 이상이 있는 값인지를 확인한다.
5. 이상이 있을 경우 hack임을 , 이상이 없을 경우 normal user임을 output한다.

main-> getframe -> get feature -> distance -> machine learning
추가적으로 이해를 도울 sequence diagram을 첨부했습니다.

test를 위한 동영상과 weights파일은 원드라이브에 있어, 링크를 첨부했습니다.


