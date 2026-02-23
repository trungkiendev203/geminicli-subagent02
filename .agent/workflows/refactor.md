---
description: Quy trình kiểm tra và tối ưu hóa mã nguồn (Refactor Workflow)
---

1. **Phân tích hiện trạng**:
   Sử dụng công cụ `grep_search` để tìm các hàm có độ dài > 50 dòng.
2. **Lập kế hoạch tách nhỏ**:
   Xác định các đoạn code có thể tách ra thành các hàm helper riêng biệt.

// turbo 3. **Thực hiện Refactor**:
Sử dụng `replace_file_content` hoặc `multi_replace_file_content` để áp dụng các thay đổi.

4. **Kiểm tra cú pháp**:
   Chạy lệnh `python -m py_compile` (cho Python) hoặc `tsc` (cho TS) để đảm bảo không có lỗi cú pháp mới.

5. **Cập nhật tài liệu**:
   Nếu có thay đổi API, hãy cập nhật vào các file tài liệu liên quan.
