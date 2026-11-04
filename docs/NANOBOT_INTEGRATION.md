# Hướng dẫn tích hợp Nanobot

## 1. Mô hình kết nối

Sổ Thu Chi vẫn là ứng dụng desktop Tkinter và tiếp tục lưu dữ liệu bằng JSON trên máy. Khi người dùng mở **Trợ lý AI**, mô-đun `ai_assistant.py` tạo một bản tóm tắt thu chi rồi gửi câu hỏi và bản tóm tắt đó tới API local của Nanobot.

```text
Người dùng
   |
   v
Giao diện Tkinter (gui.py)
   |
   v
ai_assistant.py ---- số liệu tổng hợp ----> Nanobot API local
   |                                         |
   |<----------- câu trả lời AI -------------|
   v
Hiển thị câu trả lời trong cửa sổ chat
```

Bản thử nghiệm chỉ gửi tổng thu, tổng chi, số dư, tổng chi theo danh mục và ngân sách. Ghi chú và từng bản ghi giao dịch không được gửi. Người dùng không cần nhập API key của nhà cung cấp mô hình vào Sổ Thu Chi; phần cấu hình mô hình nằm trong Nanobot.

## 2. Chuẩn bị Nanobot

Nanobot yêu cầu Python 3.11 trở lên. Nên cài Nanobot trong môi trường Python riêng, không cài lẫn vào môi trường đang dùng cho Sổ Thu Chi.

Trong môi trường riêng của Nanobot, cài bản có hỗ trợ API:

```powershell
py -m pip install "nanobot-ai[api]"
```

Nếu đã cài Nanobot theo cách khác, hãy dùng đúng môi trường Python nơi lệnh `nanobot` đang hoạt động và bổ sung extra API theo hướng dẫn chính thức.

Cấu hình nhà cung cấp và mô hình AI theo hướng dẫn Nanobot:

```powershell
nanobot onboard --wizard
```

Sau khi cấu hình xong, kiểm tra Nanobot trả lời được trước khi chạy Sổ Thu Chi. Sau đó bật API:

```powershell
nanobot serve
```

Theo tài liệu Nanobot, API mặc định lắng nghe tại `127.0.0.1:8900`, với endpoint chat completions là:

```text
http://127.0.0.1:8900/v1/chat/completions
```

Giữ cửa sổ terminal chạy Nanobot mở trong lúc sử dụng trợ lý AI. Không mở API ra mạng công cộng; bản tích hợp này chỉ cần kết nối local trên cùng máy.

Tài liệu: [Nanobot README](https://github.com/HKUDS/nanobot) · [OpenAI-compatible API](https://github.com/HKUDS/nanobot/blob/main/docs/openai-api.md).

## 3. Chạy Sổ Thu Chi

Mở một cửa sổ PowerShell khác, vào thư mục dự án và chạy:

```powershell
py gui.py
```

Tại sảnh chính, chọn **Trợ lý AI**, nhập câu hỏi rồi nhấn Enter hoặc nút **Gửi**.

Ví dụ câu hỏi:
- Tháng này tổng chi của tôi là bao nhiêu?
- Danh mục nào đang chi nhiều nhất?
- Dựa trên ngân sách hiện tại, tôi nên chú ý điều gì?

## 4. Cấu hình địa chỉ API

Mặc định ứng dụng kết nối tới `http://127.0.0.1:8900/v1/chat/completions`. Nếu Nanobot được cấu hình dùng địa chỉ khác, đặt biến môi trường trước khi mở ứng dụng:

```powershell
$env:SOTHUCHI_NANOBOT_URL = "http://127.0.0.1:8900/v1/chat/completions"
py gui.py
```

Thay địa chỉ trong ví dụ bằng endpoint thực tế của bạn nếu đã đổi host hoặc port.

## 5. Phạm vi và lưu ý

- Nanobot cần một nhà cung cấp mô hình AI đã được cấu hình; cài Nanobot không đồng nghĩa đã có mô hình miễn phí.
- Dịch vụ mô hình có thể có giới hạn hoặc chi phí riêng theo nhà cung cấp. Hãy kiểm tra điều khoản và mức sử dụng trước khi dùng.
- Nếu Nanobot chưa chạy, cửa sổ chat sẽ báo lỗi kết nối; các chức năng ghi thu chi vẫn dùng riêng như trước.
- AI chỉ đưa ra gợi ý tham khảo, không phải tư vấn tài chính chuyên nghiệp.
- Bản hiện tại không cho AI tự thêm, sửa hoặc xóa giao dịch.
- Dù đã giới hạn dữ liệu gửi đi, danh mục chi và số liệu tổng hợp vẫn là thông tin tài chính. Chỉ bật AI khi bạn đồng ý gửi các thông tin đó tới mô hình đã cấu hình.
- Trước khi thử nghiệm, hãy sao lưu `transactions.json` và `monthly_budgets.json`.

## 6. Kiểm thử

Chạy bộ test từ thư mục gốc của dự án:

```powershell
py -m pip install -r requirements-dev.txt
py -m pytest -q
```

Các test của trợ lý kiểm tra việc tạo bản tóm tắt và xử lý câu hỏi rỗng; chúng không thay thế kiểm thử kết nối thực tế với một máy Nanobot đang chạy.
