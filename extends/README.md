# MediaPipe Tracking System

## Giới thiệu

Hệ thống tracking trong thư mục này sử dụng thư viện [MediaPipe](https://mediapipe.dev/) để nhận diện và theo dõi bàn tay và khuôn mặt theo thời gian thực từ webcam. File `mediapipe-hand.py` là ví dụ minh họa cho việc kết hợp nhận diện bàn tay và lưới khuôn mặt (face mesh) cùng lúc.

## Chức năng chính

- **Nhận diện bàn tay:** Xác định vị trí các điểm đặc trưng (landmarks) trên bàn tay, vẽ các điểm và kết nối lên hình ảnh webcam.
- **Nhận diện khuôn mặt:** Xác định các điểm đặc trưng trên khuôn mặt, vẽ lưới tam giác (tessellation), đường viền khuôn mặt (contours) và tròng mắt (irises).
- **Hiển thị trực tiếp:** Kết quả được hiển thị trực tiếp trên cửa sổ webcam, hình ảnh được lật ngang như gương để dễ quan sát.

## Ứng dụng

- Phát triển các trò chơi, ứng dụng tương tác sử dụng cử chỉ tay hoặc nhận diện khuôn mặt.
- Hỗ trợ các dự án về thực tế tăng cường (AR), điều khiển không chạm, nhận diện biểu cảm khuôn mặt, v.v.

## Yêu cầu

- Python 3.x
- Thư viện OpenCV (`cv2`)
- Thư viện MediaPipe

## Cách sử dụng

1. Cài đặt các thư viện cần thiết:
   ```
   pip install opencv-python mediapipe
   ```
2. Chạy file `mediapipe-hand.py`:
   ```
   python mediapipe-hand.py
   ```
3. Đưa bàn tay hoặc khuôn mặt vào trước webcam để xem kết quả tracking.

## Ghi chú

- Nhấn phím `ESC` để thoát chương trình.
- Hệ thống chỉ nhận diện tối đa 1 khuôn mặt và nhiều bàn tay cùng lúc.
