# 📒 Sổ thu chi cá nhân

> Một dự án nhỏ mình làm để luyện Python bằng một việc khá quen thuộc: ghi lại tiền vào, tiền ra, rồi xem cuối cùng còn bao nhiêu.

Chương trình hiện chạy ngay trong terminal, chưa cần giao diện hay cài thêm thư viện. Mình sẽ bổ sung tính năng theo những phần Python học được trên lớp.

## Làm được gì rồi?

- Thêm một khoản thu hoặc chi.
- Ghi số tiền, danh mục và ghi chú.
- Xem lại các giao dịch đã nhập.
- Tính tổng thu, tổng chi và số dư.
- Báo khi nhập số tiền không hợp lệ.

## Chạy thử

Cần cài Python 3. Mở PowerShell tại thư mục dự án và chạy:

```powershell
py app.py
```

Nếu máy bạn nhận lệnh `python`, có thể dùng `python app.py`.

## Dùng chương trình

Trong menu, chọn:

- `1` để thêm giao dịch
- `2` để xem danh sách
- `3` để xem tổng kết
- `0` để thoát

Ví dụ: chọn `1`, chọn khoản chi, nhập `50000`, danh mục `Ăn uống`, rồi xem khoản đó xuất hiện trong danh sách và tổng kết.

## Tiến độ

Đây mới là bản đầu tiên. Các khoản giao dịch đang được giữ trong bộ nhớ, nên sẽ mất khi thoát chương trình. Phần mình muốn làm tiếp là lưu dữ liệu vào file để mở lại chương trình vẫn xem được lịch sử.

## Mã nguồn

- `app.py` — chương trình chính
- `requirements.txt` — hiện không cần cài thư viện ngoài
- `.gitignore` — các file Git bỏ qua

Mình làm dự án này để vừa học Python vừa có một sản phẩm nhỏ để cập nhật qua từng tuần. Nếu có góp ý, mình rất sẵn lòng nghe!
