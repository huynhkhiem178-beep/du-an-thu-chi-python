<div align="center">

# 📒 Sổ Thu Chi Cá Nhân

**Một dự án nhỏ luyện Python bằng việc quen thuộc: ghi lại tiền vào, tiền ra, rồi xem cuối cùng còn bao nhiêu.**
s
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-đang%20phát%20triển-yellow?style=flat-square)
![Platform](https://img.shields.io/badge/chạy%20trên-Terminal-lightgrey?style=flat-square)

</div>

---

Chương trình hiện chạy ngay trong terminal, chưa cần giao diện hay cài thêm thư viện. Mình sẽ bổ sung tính năng dần theo những phần Python học được trên lớp.

## ✨ Làm được gì rồi?

| Tính năng | Mô tả |
|---|---|
| ➕ Thêm giao dịch | Ghi số tiền, danh mục và ghi chú cho một khoản thu hoặc chi |
| 📋 Xem danh sách | Xem lại toàn bộ các giao dịch đã nhập |
| 📊 Xem tổng kết | Tính tổng thu, tổng chi và số dư hiện tại |
| ⚠️ Kiểm tra dữ liệu | Báo lỗi khi nhập số tiền không hợp lệ |

## 🚀 Chạy thử

Cần cài **Python 3**. Mở PowerShell tại thư mục dự án và chạy:

```powershell
py app.py
```

> Nếu máy bạn nhận lệnh `python` thay vì `py`, dùng `python app.py`.

## 🧭 Dùng chương trình

Sau khi chạy, bạn sẽ thấy menu với các lựa chọn:

| Phím | Chức năng |
|:---:|---|
| `1` | Thêm giao dịch |
| `2` | Xem danh sách |
| `3` | Xem tổng kết |
| `0` | Thoát |

**Ví dụ:** chọn `1` → chọn khoản chi → nhập `50000` → danh mục `Ăn uống` → khoản đó sẽ xuất hiện trong danh sách và tổng kết.

## 🛠️ Tiến độ

Đây mới là bản đầu tiên. Các giao dịch hiện đang được giữ **trong bộ nhớ**, nên sẽ mất khi thoát chương trình.

**Sắp làm tiếp:**
- [ ] Lưu dữ liệu vào file để mở lại chương trình vẫn xem được lịch sử

## 📂 Mã nguồn

```
.
├── app.py             # Chương trình chính
├── requirements.txt   # Hiện không cần cài thư viện ngoài
└── .gitignore          # Các file Git bỏ qua
```

---

<div align="center">

Dự án này được làm để vừa học Python vừa có một sản phẩm nhỏ cập nhật qua từng tuần.
Mọi góp ý đều rất được hoan nghênh! 💬

</div>