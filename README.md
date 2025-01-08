# Phát triển game xếp gạch trên web sử dụng MediaPipe với tương tác điều khiển bằng cử chỉ tay

## Mô tả đồ án

Đây là đồ án phát triển một trò chơi xếp gạch (Tetris) trên nền tảng web, sử dụng **MediaPipe** để nhận diện cử chỉ tay và điều khiển các thao tác trong game. Thay vì dùng bàn phím hoặc chuột, người chơi có thể điều khiển game thông qua các cử chỉ tay, mang đến một trải nghiệm chơi game mới lạ và hấp dẫn.

## Các tính năng chính

- **Điều khiển bằng cử chỉ tay**: Sử dụng MediaPipe để nhận diện các cử chỉ tay và sử dụng chúng để điều khiển các thao tác như xoay, di chuyển và rơi gạch.
- **Chơi game xếp gạch**: Trò chơi hoạt động theo các quy tắc truyền thống của game xếp gạch, nơi người chơi phải xếp các khối gạch vào các ô để xóa các dòng hoàn chỉnh.
- **Giao diện người dùng thân thiện**: Giao diện được thiết kế đơn giản và dễ sử dụng với các thông tin về điểm số và level.
- **Hỗ trợ hiệu ứng và âm thanh**: Các hiệu ứng xóa hàng, điểm thưởng, âm thanh đặc biệt như tiếng gạch rơi, xóa hàng giúp cải thiện trải nghiệm chơi game.
## Các bước thực hiện đồ án
### Bước 1: Nghiên cứu và thu thập thông tin
- Tìm hiểu về trò chơi xếp gạch, bao gồm luật chơi, các cơ chế điều khiển, và cách hoạt động.  
- Nghiên cứu Firebase Realtime Database để lưu thông tin người chơi.  
- Nghiên cứu về công nghệ MediaPipe, tập trung vào khả năng nhận diện cử chỉ tay và tích hợp trên nền tảng web.  
- Tìm hiểu các công nghệ web cần thiết như HTML, CSS, JS để xây dựng giao diện và logic trò chơi.  
- Khảo sát các game xếp gạch có sẵn để phân tích ưu, nhược điểm và định hướng cải tiến.
### Bước 2: Phân tích yêu cầu và thiết kế hệ thống
- Phân tích yêu cầu:  
	+ Xác định các cử chỉ tay cần nhận diện để thực hiện các hành động như: di chuyển, xoay, thả gạch xuống nhanh.  
	+ Xác định các tính năng chính của game, như bắt đầu, chơi, lưu điểm và kết thúc.  
- Thiết kế hệ thống kiến trúc tổng quan bao gồm:  
	+ Phần giao diện (Front-end): Xây dựng bố cục game, bảng điểm, và hiển thị gạch.  
	+ Phần xử lý cử chỉ: Tích hợp MediaPipe để xử lý dữ liệu từ camera.  
	+ Phần logic game: Điều khiển chuyển động của các khối gạch dựa trên cử chỉ.  
	+ Thiết kế giao diện người dùng trực quan, dễ sử dụng.  
### Bước 3: Xây dựng hệ thống
- Phát triển giao diện web:  
	+ Sử dụng HTML và CSS để xây dựng bố cục game, bao gồm giao diện nhập tên người chơi và giao diện chơi game, đảm bảo tính thẩm mỹ và trực quan.  
	+ Sử dụng JS để tạo hiệu ứng động và lập trình các logic game.  
- Xây dựng logic game:  
	+ Lập trình các logic game như di chuyển, xoay khối gạch, thả gạch xuống nhanh.  
 	+ Xử lý các quy tắc chơi game như xóa hàng sau khi hoàn thành một hay nhiều hàng, cập nhật điểm số, điểm cao nhất, cập nhật tên người chơi lên bảng xếp hạng, lưu điểm và kết thúc trò chơi.  
- Tích hợp MediaPipe:  
	+ Cài đặt thư viện MediaPipe để cấu hình nhận diện cử chỉ tay thông qua camera trên thiết bị của người chơi.  
	+ Xử lí dữ liệu cử chỉ tay để chuyển đổi thành lệnh điều khiển (di chuyển, xoay, thả gạch xuống nhanh).  
- Tích hợp Firebase Realtime Database để lưu thông tin người chơi.  
### Bước 4: Kiểm thử và tối ưu hóa  
- Đảm bảo các cử chỉ tay được nhận diện chính xác và phản hồi đúng trong trò chơi.  
- Kiểm tra tính chính xác của các tính năng game (di chuyển, xoay, thả gạch xuống nhanh, xóa hàng, điểm số,…).  
### Bước 5: Hoàn thiện và tích hợp tích năng bổ sung  
- Cải thiện giao diện và trải nghiệm người dùng (thêm âm thanh, hiệu ứng, bảng xếp hạng).  
- Thiết kế hướng dẫn cho người chơi.  
## Thông tin liên hệ
- Sinh viên thực hiện: Nguyễn Duy Tín  
- Lớp: DA22TTA  
- MSSV: 110122182  
- Email: duytinnguyen84@gmail.com  
- Số điện thoại: 0794325729


