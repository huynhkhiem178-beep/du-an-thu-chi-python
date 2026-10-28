<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:3776AB,100:22c55e&height=200&section=header&text=S%E1%BB%95%20Thu%20Chi%20C%C3%A1%20Nh%C3%A2n&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Luy%E1%BB%87n%20Python%20qua%20m%E1%BB%99t%20vi%E1%BB%87c%20quen%20thu%E1%BB%99c%3A%20ghi%20thu%20chi%2C%20xem%20s%E1%BB%91%20d%C6%B0&descAlignY=58&descSize=18" />

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=20&duration=3000&pause=800&color=22C55E&center=true&vCenter=true&width=650&lines=Ghi+thu+chi+%E2%86%92+L%C6%B0u+d%E1%BB%AF+li%E1%BB%87u;L%E1%BB%8Dc+theo+th%C3%A1ng+%E2%86%92+Xem+t%E1%BB%95ng+k%E1%BA%BFt;M%E1%BB%99t+d%E1%BB%B1+%C3%A1n+nh%E1%BB%8F+c%E1%BA%ADp+nh%E1%BA%ADt+m%E1%BB%97i+tu%E1%BA%A7n" alt="Typing SVG" />

<br>

[![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Terminal](https://img.shields.io/badge/Ch%E1%BA%A1y%20tr%C3%AAn-Terminal-lightgrey?style=for-the-badge&logo=windowsterminal&logoColor=white)](#-ch%E1%BA%A1y-ch%C6%B0%C6%A1ng-tr%C3%ACnh)
[![Status](https://img.shields.io/badge/Tr%E1%BA%A1ng%20th%C3%A1i-%C4%90ang%20ph%C3%A1t%20tri%E1%BB%83n-f59e0b?style=for-the-badge)](#-h%C6%B0%E1%BB%9Bng-ph%C3%A1t-tri%E1%BB%83n)
[![Author](https://img.shields.io/badge/Author-Hu%E1%BB%B3nh%20Khi%C3%AAm-e11d48?style=for-the-badge&logo=github&logoColor=white)](https://github.com/huynhkhiem178-beep)

</div>

---

## 📒 Giới thiệu

**Sổ thu chi cá nhân** là ứng dụng Python chạy trên máy tính. Ứng dụng có giao diện cửa sổ Tkinter và vẫn giữ phiên bản terminal để thực hành các thao tác bằng menu. Mình làm dự án này để ghi lại tiền thu, tiền chi, rồi xem số dư còn lại.

Giao dịch và ngân sách được lưu trên máy bằng các file JSON. Khi thoát rồi mở lại ứng dụng, dữ liệu đã lưu vẫn còn. Dự án dùng thư viện có sẵn của Python, không cần cài package ngoài.

## ✨ Chức năng hiện có

| Tính năng | Mô tả |
|---|---|
| 🖥️ Giao diện desktop | Sảnh riêng và màn hình riêng cho từng chức năng |
| ➕ Thêm giao dịch | Ghi khoản thu hoặc chi, số tiền, danh mục, ngày và ghi chú |
| 📋 Xem danh sách | Hiển thị tất cả giao dịch theo thứ tự trong file |
| 📊 Tổng kết | Tính tổng thu, tổng chi và số dư của toàn bộ giao dịch |
| 🗓️ Lọc theo tháng | Chỉ hiển thị giao dịch thuộc tháng được chọn |
| 🏷️ Lọc theo danh mục | Tìm theo toàn bộ hoặc một phần tên danh mục |
| 🧮 Tổng kết tháng | Tính riêng tổng thu, tổng chi và số dư trong một tháng |
| 🎯 Ngân sách tháng | Đặt hạn mức chi riêng cho từng tháng và xem cảnh báo khi vượt mức |
| ⭐ Đánh giá ứng dụng | Chọn từ 1–5 sao, viết góp ý và mở email đã soạn sẵn để gửi |
| ✏️ Sửa giao dịch | Cập nhật loại, số tiền, danh mục, ngày hoặc ghi chú của giao dịch đã lưu |
| 🗑️ Xóa giao dịch | Xóa giao dịch dựa trên số thứ tự trong danh sách |
| 💾 Lưu tự động | Ghi giao dịch và ngân sách vào các file JSON riêng |

## 🚀 Chạy chương trình

### Yêu cầu

- Python 3.8 trở lên.
- Windows, macOS hoặc Linux có terminal.
- Không cần cài Flask hay thư viện bên ngoài.

### Trên Windows

Mở giao diện cửa sổ bằng lệnh:

```powershell
py gui.py
```

Muốn chạy phiên bản terminal thì dùng:

```powershell
py app.py
```

### Đóng gói thành ứng dụng Windows (.exe)

Giao diện hiện tại đã là ứng dụng desktop. Nếu muốn mở app mà không gõ lệnh Python, có thể đóng gói thành `.exe` bằng PyInstaller. Mở PowerShell tại thư mục dự án và chạy:

```powershell
py -m pip install pyinstaller
py -m PyInstaller --noconfirm --clean --windowed --onedir --name SoThuChi gui.py
```

Sau khi đóng gói xong, mở `dist\SoThuChi\SoThuChi.exe`. Hãy giữ nguyên cả thư mục `SoThuChi`; các file `transactions.json` và `monthly_budgets.json` sẽ được tạo cạnh file `.exe` để dữ liệu còn sau khi tắt app. Nếu muốn mang dữ liệu hiện có sang bản `.exe`, chép `transactions.json` và `monthly_budgets.json` (nếu có) vào thư mục `dist\SoThuChi` trước lần mở đầu tiên. Không đưa dữ liệu cá nhân vào GitHub nếu không muốn chia sẻ chúng.

Nếu cửa sổ giao diện không mở, kiểm tra Tkinter bằng lệnh `py -m tkinter`. Python sẽ mở một cửa sổ mẫu nếu Tkinter đã sẵn sàng. Tkinter là giao diện Python cho bộ công cụ Tk và thường được cài cùng Python trên Windows. [Tài liệu Tkinter](https://docs.python.org/3/library/tkinter.html)

## 🖥️ Dùng giao diện desktop

Khi mở app, sảnh giới thiệu dự án và hiển thị tổng thu, tổng chi, số dư. Chọn một chức năng để mở màn hình riêng; nút **Sảnh chính** đưa bạn quay lại.

- **Thêm giao dịch:** nhập loại, số tiền, danh mục, ngày và ghi chú. Ngày dùng định dạng `YYYY-MM-DD`; số tiền phải là số nguyên dương.
- **Sổ giao dịch:** xem danh sách, lọc theo tháng hoặc tìm theo toàn bộ hay một phần tên danh mục. Chọn một dòng rồi bấm **Sửa đã chọn** hoặc nhấp đúp để chỉnh sửa. Bấm **Xóa giao dịch đã chọn** (hoặc nhấn `Delete`) để xóa; app sẽ hỏi xác nhận.
- **Báo cáo thu chi:** xem tổng thu, tổng chi và số dư của toàn bộ dữ liệu hoặc chọn tháng để xem báo cáo riêng.
- **Ngân sách tháng:** chọn tháng để xem số đã chi và hạn mức. Có thể đặt hoặc sửa hạn mức; thanh tiến độ chuyển đỏ khi chi vượt hạn mức.
- **Đánh giá ứng dụng:** chọn số sao, nhập góp ý rồi bấm **Mở email để gửi đánh giá**. App mở ứng dụng email mặc định với người nhận, tiêu đề và nội dung đã điền. Kiểm tra email rồi tự bấm **Gửi**. Máy cần có ứng dụng email mặc định được cấu hình.

Giao diện dùng chung dữ liệu với phiên bản terminal. Các giao dịch và ngân sách vẫn được lưu trong các file JSON trên máy.

## ⌨️ Phiên bản terminal

Chạy `py app.py` để dùng menu terminal. Phiên bản này dùng chung các file dữ liệu với giao diện desktop.

### Menu và cách sử dụng

| Phím | Chức năng |
|:---:|---|
| `1` | Thêm giao dịch |
| `2` | Xem tất cả giao dịch |
| `3` | Xem tổng kết |
| `4` | Lọc giao dịch theo tháng |
| `5` | Lọc giao dịch theo danh mục |
| `6` | Xem tổng kết theo tháng |
| `7` | Xóa giao dịch |
| `8` | Đặt hoặc tắt ngân sách cho một tháng |
| `9` | Sửa thông tin giao dịch |
| `0` | Thoát chương trình |

### 1. Thêm khoản thu hoặc chi

Chọn `1`, rồi nhập lần lượt:

1. Loại giao dịch: `1` cho khoản thu hoặc `2` cho khoản chi.
2. Số tiền: nhập số nguyên dương, đơn vị VND.
3. Danh mục: ví dụ `Luong`, `An uong`, `Hoc tap`.
4. Ngày: theo mẫu `YYYY-MM-DD`, ví dụ `2026-09-28`. Nhấn Enter để dùng ngày hiện tại.
5. Ghi chú: có thể mô tả ngắn hoặc để trống.

Ví dụ một giao dịch chi:

```text
Loai giao dich: 2
So tien: 50000
Danh muc: An uong
Ngay: 2026-09-28
Ghi chu: Bua trua
```

Sau khi nhập hợp lệ, giao dịch được thêm vào danh sách và lưu xuống file JSON.

### 2. Xem tất cả giao dịch

Chọn `2`. Mỗi dòng hiển thị ngày, loại giao dịch, danh mục, số tiền có dấu cộng/trừ và ghi chú nếu có.

Ví dụ:

```text
1. 2026-09-28 | Chi | An uong | -50,000 VND | Bua trua
2. 2026-09-28 | Thu | Lam them | +300,000 VND
```

### 3. Xem tổng kết

Chọn `3` để tính trên toàn bộ giao dịch đã lưu:

- **Tổng thu** là tổng số tiền của các giao dịch loại Thu.
- **Tổng chi** là tổng số tiền của các giao dịch loại Chi.
- **Số dư** được tính bằng tổng thu trừ tổng chi.

Số dư có thể âm nếu tổng chi lớn hơn tổng thu.

### 4. Lọc giao dịch theo tháng

Chọn `4` và nhập tháng dạng `YYYY-MM`, ví dụ `2026-09`. Chương trình chỉ hiển thị các giao dịch có ngày thuộc tháng đó.

### 5. Lọc giao dịch theo danh mục

Chọn `5` rồi nhập tên hoặc một phần tên danh mục. Bộ lọc không phân biệt chữ hoa và chữ thường. Ví dụ, nhập `an` có thể tìm được danh mục `An uong`.

### 6. Xem tổng kết theo tháng

Chọn `6` rồi nhập tháng dạng `YYYY-MM`. Kết quả là tổng thu, tổng chi và số dư chỉ tính từ các giao dịch trong tháng đó.

Nếu đã đặt ngân sách cho tháng này, phần tổng kết cũng hiển thị hạn mức, số tiền còn lại hoặc số tiền đã vượt.

### 7. Xóa giao dịch

Chọn `7` để in danh sách kèm số thứ tự. Nhập số thứ tự của giao dịch muốn xóa. Việc xóa được lưu ngay vào file dữ liệu.

> Lưu ý: chương trình xóa theo số thứ tự đang hiển thị trong danh sách, không có bước hỏi xác nhận.

### 8. Đặt ngân sách tháng

Chọn `8`, nhập tháng dạng `YYYY-MM`, rồi nhập hạn mức chi bằng VND. Ví dụ, đặt `250000` cho tháng `2026-09`. Khi xem tổng kết tháng 9, app so tổng chi với hạn mức. Nếu tổng chi lớn hơn ngân sách, app báo số tiền vượt.

Nhập `0` làm hạn mức để tắt ngân sách của tháng đó. Mỗi tháng có hạn mức riêng; ngân sách được lưu trong `monthly_budgets.json`.

### 9. Sửa thông tin giao dịch

Chọn `9`, nhập số thứ tự của giao dịch muốn sửa. Với mỗi trường, nhấn Enter để giữ giá trị hiện tại. Nhập `1` cho khoản thu hoặc `2` cho khoản chi; số tiền phải là số nguyên dương và ngày phải đúng dạng `YYYY-MM-DD`. Ở phần ghi chú, nhập `-` nếu muốn xóa ghi chú. Thông tin mới được lưu vào `transactions.json`.

## 🗓️ Định dạng và kiểm tra dữ liệu

Chương trình kiểm tra một số dữ liệu cơ bản trước khi ghi:

- Số tiền phải là số nguyên lớn hơn 0.
- Danh mục không được để trống.
- Ngày phải hợp lệ và theo dạng `YYYY-MM-DD`.
- Tháng lọc phải theo dạng `YYYY-MM`.
- Nếu nhập sai số tiền hoặc ngày, chương trình báo lỗi và không thêm giao dịch đó.

Số tiền hiện được lưu bằng số nguyên VND, chưa hỗ trợ số lẻ hoặc ngoại tệ.

## 💾 Cách lưu dữ liệu

File `transactions.json` nằm cùng thư mục với `app.py`. File được tạo khi lưu giao dịch đầu tiên. Khi khởi động, chương trình đọc file này; khi thêm, sửa hoặc xóa giao dịch, chương trình ghi danh sách mới vào file.

Một giao dịch trong file có dạng:

```json
{
  "kind": "Chi",
  "amount": 50000,
  "category": "An uong",
  "day": "2026-09-28",
  "note": "Bua trua"
}
```

Các trường có ý nghĩa:

| Trường | Nội dung |
|---|---|
| `kind` | Loại giao dịch: `Thu` hoặc `Chi` |
| `amount` | Số tiền nguyên dương, tính bằng VND |
| `category` | Danh mục do người dùng nhập |
| `day` | Ngày theo dạng `YYYY-MM-DD` |
| `note` | Ghi chú; có thể là chuỗi rỗng |

Dữ liệu tài chính là dữ liệu cá nhân, vì vậy `transactions.json` đã được thêm vào `.gitignore` và không nên đẩy lên GitHub. File `sample_transactions.json` chỉ chứa dữ liệu giả lập và có thể đưa lên repository.

Ngân sách theo tháng được lưu riêng trong `monthly_budgets.json`, theo dạng tháng và số tiền:

```json
{
  "2026-09": 250000
}
```

File ngân sách cũng bị Git bỏ qua vì đây là thiết lập cá nhân. Hai file JSON được tạo tự động khi ứng dụng cần lưu dữ liệu lần đầu.

## 🧪 Thử bằng dữ liệu mẫu

File `sample_transactions.json` có 9 giao dịch giả lập thuộc tháng 8 và tháng 9 năm 2026. Cách thử dưới đây sao lưu file dữ liệu cá nhân nếu file đó đã có:

```powershell
if (Test-Path .\transactions.json) {
    Copy-Item .\transactions.json ..\transactions-backup-before-demo.json
}
if (Test-Path .\monthly_budgets.json) {
    Copy-Item .\monthly_budgets.json ..\monthly-budgets-backup-before-demo.json
}
Copy-Item .\sample_transactions.json .\transactions.json -Force
py app.py
```

Các bước chọn mục menu bên dưới dành cho phiên bản terminal. Muốn mở cửa sổ giao diện với cùng dữ liệu mẫu, dùng `py gui.py` thay cho `py app.py`.

Sau khi mở ứng dụng, thử các mục sau:

1. Chọn `2` để xem danh sách.
2. Chọn `3` để xem tổng kết toàn bộ.
3. Chọn `4`, nhập `2026-09` để lọc tháng 9.
4. Chọn `5`, nhập `An uong` để lọc danh mục.
5. Chọn `6`, nhập `2026-09` để xem tổng kết tháng.
6. Chọn `7` để xóa một giao dịch mẫu.
7. Chọn `8`, đặt ngân sách tháng `2026-09` là `250000`, rồi dùng mục `6` xem cảnh báo vượt ngân sách.

Kết quả tháng 9 với dữ liệu mẫu:

| Khoản | Số tiền |
|---|---:|
| Tổng thu | 9.000.000 VND |
| Tổng chi | 290.000 VND |
| Số dư | 8.710.000 VND |

Tháng 8 có tổng thu `500.000 VND`, tổng chi `410.000 VND`, số dư `90.000 VND`.

Nếu đặt ngân sách tháng 9 là `250.000 VND`, app sẽ báo đã vượt `40.000 VND` vì tổng chi tháng đó là `290.000 VND`.

Để khôi phục dữ liệu trước khi thử:

```powershell
if (Test-Path ..\transactions-backup-before-demo.json) {
    Copy-Item ..\transactions-backup-before-demo.json .\transactions.json -Force
} else {
    Remove-Item .\transactions.json
}
if (Test-Path ..\monthly-budgets-backup-before-demo.json) {
    Copy-Item ..\monthly-budgets-backup-before-demo.json .\monthly_budgets.json -Force
} else {
    Remove-Item .\monthly_budgets.json -ErrorAction SilentlyContinue
}
```

## 🧠 Python áp dụng trong dự án

| Kiến thức | Được dùng ở đâu |
|---|---|
| Biến và kiểu dữ liệu | Lưu số tiền, loại giao dịch, ngày và danh mục |
| `if/elif/else` | Xử lý lựa chọn trong menu và kiểm tra dữ liệu |
| Vòng lặp `while` | Giữ menu hoạt động cho đến khi người dùng chọn thoát |
| List và dictionary | Lưu nhiều giao dịch và các trường của từng giao dịch |
| Hàm | Chia chương trình thành thao tác thêm, xem, lọc, tính và xóa |
| List comprehension | Tạo danh sách giao dịch phù hợp với bộ lọc |
| `try/except` | Báo lỗi khi chuyển số, kiểm tra ngày hoặc đọc JSON |
| File I/O và JSON | Đọc dữ liệu khi mở app, ghi dữ liệu sau khi thay đổi |
| Thư viện chuẩn | `datetime.date` kiểm tra ngày; `pathlib.Path` xác định vị trí file |
| Dictionary theo tháng | Lưu ngân sách riêng cho từng tháng |
| Tkinter và ttk | Tạo cửa sổ, form nhập liệu, bảng giao dịch và hộp thoại xác nhận |

Các hàm chính trong `app.py`:

- `load_transactions()` và `save_transactions()`: đọc và ghi dữ liệu.
- `add_transaction()`: nhập, kiểm tra và thêm giao dịch.
- `show_transactions()` và `show_summary()`: in danh sách và tính tổng.
- `get_transactions_for_month()`: tạo danh sách giao dịch theo tháng.
- `filter_by_month()`, `filter_by_category()`: tìm giao dịch.
- `show_month_summary()`: tính tổng cho tháng được chọn.
- `load_budgets()`, `save_budgets()` và `set_monthly_budget()`: đọc, ghi và cập nhật hạn mức từng tháng.
- `edit_transaction()`: cập nhật giao dịch theo số thứ tự.
- `delete_transaction()`: xóa giao dịch theo số thứ tự.
- `main()`: nạp dữ liệu và điều khiển menu.
- `gui.py`: giao diện desktop; dùng chung các hàm lưu dữ liệu trong `app.py`.

## 📂 Cấu trúc thư mục

```
.
├── app.py                   # Phiên bản terminal và lớp lưu dữ liệu
├── gui.py                   # Giao diện desktop Tkinter
├── sample_transactions.json # Bộ dữ liệu giả lập để thực hành
├── tests/
│   └── test_app.py           # Kiểm thử tự động bằng pytest
├── requirements-dev.txt     # Thư viện chỉ dùng khi phát triển
├── docs/
│   └── DEVELOPMENT.md       # Ghi chú phát triển và an toàn dữ liệu
├── .github/workflows/
│   ├── build-windows.yml    # Đóng gói ứng dụng Windows
│   └── tests.yml            # Chạy kiểm thử tự động
├── transactions.json        # Dữ liệu cá nhân, được Git bỏ qua
├── monthly_budgets.json     # Hạn mức chi cá nhân, được Git bỏ qua
├── README.md                # Mô tả và hướng dẫn
└── .gitignore               # Danh sách file Git bỏ qua
```

## 🧪 Kiểm thử tự động

Dự án có một bộ kiểm thử dùng `pytest` để kiểm tra việc xác thực dữ liệu giao dịch, định dạng tháng, đọc file JSON và lưu dữ liệu. Đây là công cụ phát triển tùy chọn; ứng dụng bình thường vẫn dùng thư viện có sẵn của Python.

Cài thư viện kiểm thử:

```powershell
py -m pip install -r requirements-dev.txt
```

Chạy kiểm thử từ thư mục gốc của dự án:

```powershell
py -m pytest -q
```

GitHub Actions cũng tự chạy các kiểm thử này khi có thay đổi liên quan đến mã nguồn hoặc bộ test. Kết quả kiểm thử tự động không thay thế việc chạy thử giao diện trên Windows.

**Lưu ý dữ liệu:** ứng dụng kiểm tra cấu trúc giao dịch và ngân sách khi đọc JSON; thao tác ghi sử dụng file tạm rồi thay thế file dữ liệu để giảm nguy cơ ghi dở dang. Nếu không lưu được, giao diện sẽ báo lỗi và hoàn tác thay đổi trong bộ nhớ. Bạn vẫn nên sao lưu file JSON trước khi thử nghiệm.

## 📌 Giới hạn hiện tại

- Giao diện hiện là app desktop, chưa có phiên bản điện thoại hoặc web.
- Chưa có đăng nhập hoặc đồng bộ dữ liệu giữa nhiều máy.
- Dữ liệu được lưu cục bộ trong một file JSON.
- Ngân sách chỉ đưa ra cảnh báo khi vượt hạn mức, chưa tự chặn giao dịch.
- Xóa giao dịch cập nhật file ngay và không có nút hoàn tác.

## 🛠️ Hướng phát triển

Một số ý tưởng cho các lần cập nhật sau:

- [ ] Xuất giao dịch hoặc báo cáo tháng ra CSV.
- [ ] Thống kê chi tiêu theo từng danh mục.
- [ ] Hiển thị biểu đồ thu chi theo tháng.
- [x] Bổ sung kiểm thử tự động cho xác thực dữ liệu và lưu JSON.
- [ ] Nghiên cứu tích hợp Nanobot để hỗ trợ thao tác với sổ thu chi bằng ngôn ngữ tự nhiên.

## 🤖 Định hướng tích hợp Nanobot

Mình dự định nghiên cứu tích hợp [Nanobot](https://github.com/HKUDS/nanobot) với dự án Sổ Thu Chi để thử nghiệm cách dùng trợ lý AI hỗ trợ quản lý thu chi. Đây là **kế hoạch phát triển trong tương lai**, chưa phải tính năng đã hoàn thành.

Một số chức năng có thể xem xét:

- [ ] Hỏi Nanobot về tổng thu, tổng chi và số dư theo tháng.
- [ ] Yêu cầu xem các giao dịch theo ngày hoặc danh mục.
- [ ] Hỗ trợ thêm giao dịch hoặc đặt ngân sách sau khi người dùng xác nhận.
- [ ] Giữ dữ liệu thu chi trên máy, không tự ý gửi dữ liệu cá nhân đến dịch vụ bên ngoài.

Khi triển khai, cần thiết kế một lớp kết nối rõ ràng giữa Nanobot và ứng dụng Python, kiểm tra dữ liệu đầu vào và yêu cầu xác nhận trước khi ghi thay đổi vào sổ thu chi. Việc tích hợp cũng cần được kiểm thử riêng để tránh làm ảnh hưởng các chức năng hiện có.


## 🎤 Gợi ý trình bày

Có thể demo giao diện theo thứ tự: thêm một khoản thu, thêm một khoản chi, lọc theo tháng, đặt ngân sách rồi xem cảnh báo trong tổng kết tháng. Sau đó khởi động lại ứng dụng để cho thấy dữ liệu vẫn được lưu. Khi giới thiệu code, có thể giải thích cách Tkinter nhận thao tác từ cửa sổ, cách list/dictionary giữ giao dịch và cách JSON lưu dữ liệu giữa các lần chạy.

## 🔎 Nguồn tham khảo

Ý tưởng đặt ngân sách theo tháng và cảnh báo khi chi tiêu vượt hạn mức được tham khảo từ [Bagels của EnhancedJax](https://github.com/EnhancedJax/Bagels), một ứng dụng theo dõi chi tiêu chạy trong terminal. Bagels có nhiều tính năng nâng cao; dự án này chỉ tham khảo ý tưởng ngân sách và tự triển khai bằng Python cơ bản. Không sao chép mã nguồn của Bagels.

Bagels phát hành theo giấy phép GPL-3.0. Xem repository gốc để biết thêm về dự án và giấy phép.

---

<div align="center">

Dự án nhỏ này được mình cập nhật dần trong lúc học Python. Mọi góp ý đều được hoan nghênh! 💬

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:22c55e,100:3776AB&height=120&section=footer" />

</div>
