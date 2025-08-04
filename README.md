# Giới thiệu dự án Mediapipe với các cử chỉ bám theo đối tượng

Dự án này sử dụng Mediapipe để nhận diện và theo dõi các cử chỉ tay trong không gian 3D. Hệ thống chủ yếu được phát triển bằng JavaScript cho phía client, cho phép xử lý hình ảnh từ camera, phát hiện bàn tay, nhận diện các cử chỉ và bám theo chuyển động của đối tượng trong thời gian thực. Phía server sử dụng Golang để xử lý dữ liệu, quản lý kết nối và hỗ trợ các tính năng mở rộng. Ứng dụng phù hợp cho các trò chơi, mô phỏng hoặc điều khiển tương tác bằng cử chỉ tay.

**Tính năng chính:**
- Nhận diện bàn tay và các điểm đặc trưng (landmarks)
- Theo dõi chuyển động của bàn tay và các cử chỉ
- Bám theo đối tượng được chỉ định trong môi trường 3D
- Dễ dàng tích hợp vào các dự án game hoặc mô phỏng

**Công nghệ sử dụng:**  
- [Mediapipe](https://mediapipe.dev/)
- JavaScript (client)
- Golang (server)
## Chạy server local nhanh với Python

Nếu bạn muốn chạy một server HTTP đơn giản để phục vụ file tĩnh (tương tự như các ví dụ trên), chỉ cần sử dụng lệnh sau trong thư mục mong muốn:

```bash
python -m http.server 8000
```

Server sẽ phục vụ các file tĩnh tại địa chỉ `http://localhost:8000`.
