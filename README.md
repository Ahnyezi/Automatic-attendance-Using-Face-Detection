## Automatic attendance Using Face Detection

#### 캠에 얼굴을 갖다대면 자동으로 사람 얼굴을 구분하고, 출결을 관리해주는 프로그램.
<br>

### 1) 얼굴 인식을 위한 학습 모델 구현하기.
- RecordForTrainingData() : training data를 위해 얼굴을 촬영
	이때 촬영된 사람의 이름을 한 폴더를 만들어 dataset  폴더에 저장한다.
- face_recog_train() : Dataset을 이용해 학습 모델 만들기.
	- haarcascade를 통해서 사진속 얼굴의 bounding box 추출 ⇒ samples 배열 저장
	- Dataset 폴더별로 각 얼굴 데이터를 labeling  ⇒ ids 배열 저장
	- samples 배열 & ids 배열을 이용해 Training ⇒ trainder.yml에 저장.
<br>	
	
### 2) haarcascade와 학습 모델을 이용하여 얼굴 탐지 및 구별
- face_detect() : 만들어진 학습 모델을 이용해 얼굴 인식 및 구분
	-  예측된 값의 Loss값이 40 이하 & 15번 이상 확인 될 경우 출석 처리
		- attend_chk() : 출석처리가 완료되면 "PASS"를 화면에 출력
			이미 출석되어있는 경우 "already attend" 를 화면에 출력
		- flag_switch() : 얼굴인식이 되어 출석 완료된 경우를 사용자에게 2초가량 표시할 수 있도록 해주는 thread 함수 생성.
		- upload() : Oracle Database에 접근하여 ATTEND 테이블에 얼굴이 인식된 학생의 이름과 오늘 날짜를 추가하는 함수.<br>
	<br>
	<image src="https://user-images.githubusercontent.com/34594339/88763234-c271b280-d1ad-11ea-93b4-623f38f4eca0.png" width="70%">

<br>	

### 3) 출석 확인 프로그램

- UI 구성

	<image src="https://user-images.githubusercontent.com/34594339/92508371-80736c00-f243-11ea-84d6-027cf718310d.png" width="70%">

	1) 이름과 휴대폰번호를 통해 접속(상단의 창)
	2) 접속한 학생의 오늘 출결 여부 확인(왼쪽 하단)
	3) 전체 출석 정보 보기 ( 오른쪽 하단) 
