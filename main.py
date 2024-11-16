import cv2
import torch
model = torch.hub.load('ultralytics/yolov5', 'custom', path='./yolov5m.pt',force_reload=True)  
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    results = model(frame)
    results.render()  
    cv2.imshow('Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()