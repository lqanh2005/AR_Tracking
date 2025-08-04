import cv2
import mediapipe as mp

# Khởi tạo các module hỗ trợ vẽ và nhận diện bàn tay, khuôn mặt
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh

# Mở webcam (camera mặc định)
cap = cv2.VideoCapture(0)

# Sử dụng context manager để khởi tạo và tự động giải phóng tài nguyên cho Hand và FaceMesh
with mp_hands.Hands(
    model_complexity=0,  # Độ phức tạp của mô hình (0: đơn giản, nhanh hơn)
    min_detection_confidence=0.5,  # Ngưỡng phát hiện bàn tay
    min_tracking_confidence=0.5) as hands, \
     mp_face_mesh.FaceMesh(
    max_num_faces=1,  # Số khuôn mặt tối đa nhận diện
    refine_landmarks=True,  # Làm mịn các điểm landmark
    min_detection_confidence=0.5,  # Ngưỡng phát hiện khuôn mặt
    min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        success, image = cap.read()  # Đọc một khung hình từ webcam
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image.flags.writeable = False  # Đánh dấu ảnh không thể ghi để tăng hiệu suất
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Chuyển ảnh sang RGB

        # Nhận diện bàn tay trên ảnh RGB
        hand_results = hands.process(rgb_image)
        # Nhận diện khuôn mặt trên ảnh RGB
        face_results = face_mesh.process(rgb_image)

        image.flags.writeable = True  # Cho phép ghi lên ảnh trở lại
        image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)  # Chuyển lại sang BGR để hiển thị bằng OpenCV

        # Vẽ các điểm và kết nối của bàn tay nếu phát hiện được
        if hand_results.multi_hand_landmarks:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,  # Ảnh để vẽ lên
                    hand_landmarks,  # Các điểm landmark của bàn tay
                    mp_hands.HAND_CONNECTIONS,  # Các kết nối giữa các điểm trên bàn tay
                    mp_drawing_styles.get_default_hand_landmarks_style(),  # Kiểu vẽ điểm
                    mp_drawing_styles.get_default_hand_connections_style())  # Kiểu vẽ kết nối

        # Vẽ các điểm và kết nối của khuôn mặt nếu phát hiện được
        if face_results.multi_face_landmarks:
            for face_landmarks in face_results.multi_face_landmarks:
                # Vẽ lưới tam giác (tessellation) trên khuôn mặt
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(80,220,240), thickness=1, circle_radius=1))
                # Vẽ đường viền các bộ phận khuôn mặt (contours)
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2))
                # Vẽ đường viền tròng mắt (irises)
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,255), thickness=2, circle_radius=2))

        # Hiển thị ảnh đã vẽ lên cửa sổ, lật ngang như gương
        cv2.imshow('MediaPipe Hands & Face Mesh', cv2.flip(image, 1))
        # Nếu nhấn phím ESC (mã 27), thoát vòng lặp
        if cv2.waitKey(5) & 0xFF == 27:
            break

# Giải phóng tài nguyên webcam
cap.release()