# Kết nối Sổ Thu Chi với OpenClaw (Windows)

## Chuẩn bị
1. Cập nhật/tải dự án Sổ Thu Chi về máy.
2. Đặt `openclaw_bridge.py` cùng thư mục với `app.py` và các file dữ liệu JSON.
3. Mở PowerShell và chạy (thay đường dẫn mẫu bằng đường dẫn thật):

```powershell
py "C:\duong-dan\du-an-thu-chi-python\openclaw_bridge.py" summary
py "C:\duong-dan\du-an-thu-chi-python\openclaw_bridge.py" list
```

## Cài skill
Lấy thư mục `skills/so-thu-chi` từ fork OpenClaw và đặt vào thư mục skills cá nhân được phiên bản OpenClaw đang cài sử dụng. Kiểm tra tài liệu/CLI của phiên bản đó để xác định đúng vị trí. Thay `<bridge-path>` trong hướng dẫn skill bằng đường dẫn đầy đủ thật.

## Lệnh
- `summary`: tổng thu, chi, số dư và ngân sách tháng hiện tại.
- `list --month 2026-10`: giao dịch theo tháng.
- `list --category "an uong"`: lọc danh mục.
- `add --kind Chi --amount 30000 --category "an uong" --day 2026-10-28 --note "com trua"`: thêm giao dịch.
- `set-budget --month 2026-10 --amount 1500000`: đặt ngân sách.

OpenClaw phải xin xác nhận trước mọi lệnh ghi dữ liệu. Skill không hỗ trợ xóa/sửa giao dịch cũ.

## Riêng tư
Không commit `transactions.json` hoặc `monthly_budgets.json` có dữ liệu thật lên GitHub. Không gửi chúng cho dịch vụ bên ngoài. Sao lưu trước khi thử các lệnh ghi.
