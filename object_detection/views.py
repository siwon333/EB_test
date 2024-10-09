from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import cv2
import numpy as np
from ultralytics import YOLO
from .models import DetectedObject

# YOLO 모델 로드
model = YOLO('yolov8n.pt')

# 실시간 웹캠 객체 감지 함수
def detect_objects_from_camera():
    cap = cv2.VideoCapture(0)  # 웹캠 열기
    
    # FPS 설정 (초당 10 프레임으로 제한)
    cap.set(cv2.CAP_PROP_FPS, 10)

    frame_count = 0
    skip_frames = 2  # 2개 프레임마다 1개 프레임만 처리 (프레임 드롭)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 프레임 카운팅 및 스킵
        frame_count += 1
        if frame_count % skip_frames != 0:
            continue  # 프레임 건너뜀

        # 프레임 해상도 줄이기 (성능 향상을 위해)
        frame = cv2.resize(frame, (640, 480))  # 해상도 줄이기

        # YOLOv8로 객체 감지
        results = model(frame)
        annotated_frame = results[0].plot()  # 감지된 객체가 표시된 이미지

        detected_objects = set()

        # 감지된 객체를 데이터베이스에 저장
        for result in results:
            for obj in result.boxes:
                object_name = model.names[int(obj.cls[0])]
                print(object_name)

                if object_name not in detected_objects:
                    detected_objects.add(object_name)
                    # 중복된 객체가 있으면 모두 삭제 후 새로 저장
                    DetectedObject.objects.filter(object_name=object_name).delete()
                    DetectedObject.objects.create(object_name=object_name)

        # JPEG로 인코딩
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        # 클라이언트로 프레임 전송
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# object_detection 뷰: 웹캠의 객체 탐지 스트림을 반환
@login_required
def object_detection(request):
    return StreamingHttpResponse(detect_objects_from_camera(),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
