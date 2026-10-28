# Tải bản Windows của Sổ Thu Chi

Bản Windows được build tự động bằng GitHub Actions từ mã nguồn `gui.py`, có đóng gói phần mở rộng Tkinter và các thư viện cần thiết.

## Tải ứng dụng

1. Mở tab **Actions** của repository.
2. Chọn workflow **Build Windows app**.
3. Mở lần chạy thành công gần nhất (dấu tích xanh).
4. Trong mục **Artifacts**, tải `SoThuChi-Windows`.
5. Giải nén ZIP trước khi chạy `SoThuChi/SoThuChi.exe`. Giữ nguyên toàn bộ thư mục `SoThuChi`, không chỉ chép riêng file EXE.

## Tạo bản build mới

Vào **Actions → Build Windows app → Run workflow**. Khi chạy xong, tải ZIP từ mục **Artifacts**. Artifact được lưu 30 ngày.

## Lưu ý

- Bản build dành cho Windows 64-bit runner của GitHub Actions.
- Không cần cài Python để chạy bản đã đóng gói.
- Nếu Windows SmartScreen hiện cảnh báo ứng dụng chưa được nhận diện, chỉ chạy nếu bạn tin tưởng nguồn tải và đã kiểm tra repository.
- Dữ liệu thu chi cá nhân nên được sao lưu riêng; không commit file JSON có dữ liệu riêng tư lên repository công khai.
