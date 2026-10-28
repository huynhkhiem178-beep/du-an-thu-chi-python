# Ghi chú phát triển

Tài liệu này bổ sung cho README hiện tại; không thay thế hướng dẫn chạy ứng dụng.

## Cấu trúc hiện tại

- `gui.py`: giao diện desktop Tkinter; gọi các hàm dữ liệu từ `app.py`.
- `app.py`: phiên bản terminal, xác thực giao dịch và đọc/ghi JSON.
- `transactions.json`: giao dịch cá nhân, được Git bỏ qua.
- `monthly_budgets.json`: ngân sách theo tháng, được Git bỏ qua.
- `sample_transactions.json`: dữ liệu minh họa, không chứa giao dịch cá nhân.
- `tests/test_app.py`: kiểm thử tự động cho xác thực và lưu trữ.

## Nguyên tắc an toàn dữ liệu

1. Chỉ chấp nhận giao dịch có loại `Thu` hoặc `Chi`, số tiền nguyên dương, danh mục không rỗng và ngày hợp lệ.
2. Bỏ qua bản ghi không hợp lệ khi đọc; không tự sửa hoặc ghi đè file gốc chỉ vì dữ liệu đọc vào bị lỗi.
3. Ghi JSON ra file tạm cùng thư mục rồi thay thế file đích để giảm nguy cơ file bị ghi dở dang.
4. Nếu lưu thất bại trong giao diện, hoàn tác thay đổi tương ứng trong bộ nhớ và báo cho người dùng.
5. Sao lưu JSON trước khi thử tính năng mới hoặc dùng dữ liệu demo.

## Chạy kiểm thử

Cần Python 3.8 trở lên. Cài thư viện phát triển:

```powershell
py -m pip install -r requirements-dev.txt
py -m pytest -q
```

Các bài test dùng thư mục tạm và không cần đụng vào dữ liệu cá nhân thật.

## Đóng gói Windows

Workflow `Build Windows app` tạo bản portable; workflow `Python tests` chạy kiểm thử. Sau khi thay đổi `gui.py`, `app.py` hoặc cấu hình đóng gói, hãy kiểm tra cả hai workflow và chạy thử EXE trên Windows trước khi phát hành.

## Định hướng tích hợp Nanobot

Tích hợp AI nên thông qua một lớp dịch vụ riêng, không để mô hình truy cập trực tiếp file JSON. Các thao tác đọc có thể bắt đầu từ báo cáo đã tổng hợp; thao tác thêm, sửa hoặc xóa phải xác nhận rõ ràng trước khi ghi dữ liệu. Không gửi dữ liệu tài chính riêng tư ra dịch vụ bên ngoài nếu chưa có sự đồng ý và biện pháp bảo vệ phù hợp.
