import cv2
from detector import MediaPipeDetector
# from overlays.hat_overlay import draw_hat
# from overlays.watch_overlay import draw_watch

cap = cv2.VideoCapture(0)
detector = MediaPipeDetector()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Skipping empty frame")
        continue

    frame.flags.writeable = True
    hand_results, face_results = detector.process(frame)

    # Dùng overlay mô hình nếu muốn
    # if face_results.multi_face_landmarks:
    #     draw_hat(frame, face_results.multi_face_landmarks[0])
    # if hand_results.multi_hand_landmarks:
    #     draw_watch(frame, hand_results.multi_hand_landmarks[0])

    frame = detector.draw(frame, hand_results, face_results)

    cv2.imshow('MediaPipe AR Overlay', cv2.flip(frame, 1))
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
