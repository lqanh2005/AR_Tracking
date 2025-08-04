import cv2
import mediapipe as mp

# Khởi tạo các đối tượng của thư viện MediaPipe để nhận diện pose (tư thế cơ thể)
mp_pose = mp.solutions.pose  # Lấy module pose từ mediapipe
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)  
# Tạo đối tượng pose với ngưỡng phát hiện và theo dõi là 0.5

mp_drawing = mp.solutions.drawing_utils  # Module hỗ trợ vẽ các điểm và kết nối lên hình

# Mở webcam (camera mặc định, chỉ số 0)
cap = cv2.VideoCapture(0) 
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Vòng lặp chính để đọc từng khung hình từ webcam
while cap.isOpened():
    success, frame = cap.read()  # Đọc một khung hình từ webcam
    if not success:
        print("empty camera frame.")
        continue

    # Chuyển đổi khung hình sang định dạng RGB (MediaPipe yêu cầu ảnh RGB)
    frame.flags.writeable = False  # Đánh dấu frame là không thể ghi để tăng hiệu suất
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Chuyển BGR sang RGB

    # Xử lý khung hình để phát hiện pose
    results = pose.process(rgb_frame)
    frame.flags.writeable = True  # Cho phép ghi lên frame trở lại

    # Nếu phát hiện được các điểm pose (pose_landmarks)
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame,  # Ảnh gốc để vẽ lên
            results.pose_landmarks,  # Các điểm pose phát hiện được
            mp_pose.POSE_CONNECTIONS,  # Các kết nối giữa các điểm
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),  # Định dạng vẽ điểm
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)  # Định dạng vẽ kết nối
        )

    # Hiển thị khung hình đã vẽ lên cửa sổ, lật ngang để giống gương
    cv2.imshow('MediaPipe Pose Detection', cv2.flip(frame, 1))

    # Nếu nhấn phím ESC (mã 27), thoát vòng lặp
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Giải phóng tài nguyên: đóng webcam và cửa sổ hiển thị
cap.release()
cv2.destroyAllWindows()
pose.close()