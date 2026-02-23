# 🤖 Geminicli-subagent02

> **Ví dụ về cách tạo một GeminiCLI subagent dành cho AI Agents, sẵn sàng cho giai đoạn tiếp theo là AgentsicSE.**

## 🌟 Giới thiệu

`geminicli-subagent02` là một repository mẫu (blueprint) được thiết kế để trình diễn sức mạnh của việc module hóa AI Agents thông qua **GeminiCLI Subagents**. Trong kỷ nguyên **AgentsicSE** (Agentic Software Engineering), việc chia nhỏ các tác vụ thông minh thành các subagent chuyên biệt là chìa khóa để xây dựng các hệ thống tự động hóa phần mềm quy mô lớn.

Dự án này tập trung vào vai trò **Code Architect** - một subagent có khả năng hiểu, phân tích và đề xuất cấu trúc cho các dự án phần mềm.

## 🚀 Tính năng nổi bật

- **Cấu hình Agent-Native**: Sử dụng thư mục `.agent` chuẩn để định nghĩa Persona và Brain của subagent.
- **Smart Workflows**: Hệ thống quy trình tự động hóa (Workflows) thực thi bằng ngôn ngữ tự nhiên.
- **Project Analysis Tools**: Tích hợp các script Python mạnh mẽ để quét và phân tích codebase.
- **Tính sẵn sàng cao**: Dễ dàng tích hợp vào bất kỳ dự án nào sử dụng GeminiCLI.

## 📂 Cấu trúc Repository

```text
geminicli-subagent02/
├── .agent/                 # 🧠 "Bộ não" của Subagent
│   ├── instructions.md     # Persona, quy tắc và chỉ dẫn hoạt động
│   └── workflows/          # ⚙️ Các quy trình tự động hóa
│       └── refactor.md     # Workflow mẫu về việc cấu trúc lại mã nguồn
├── scripts/                # 🛠️ Công cụ hỗ trợ Agent
│   └── analyze.py          # Script phân tích cấu trúc dự án
└── README.md               # Tài liệu hướng dẫn
```

## 🛠️ Cách sử dụng

Để sử dụng subagent này trong môi trường GeminiCLI của bạn:

1. **Clone repository này** vào thư mục dự án của bạn (hoặc sử dụng như một thư mục tham chiếu).
2. **Kích hoạt Subagent**: GeminiCLI sẽ tự động nhận diện các cấu hình trong `.agent`.
3. **Chạy Workflow**:
   ```bash
   /run refactor.md
   ```
4. **Sử dụng Script**: Agent có thể tự động gọi `python scripts/analyze.py` để lấy dữ liệu đầu vào cho quá trình suy luận.

## 🎯 Mục tiêu dự án

Dự án này phục vụ cho việc học tập và phát triển cộng đồng AI Agents tại Việt Nam, hướng tới việc xây dựng các công cụ AI không chỉ "biết code" mà còn "hiểu cách xây dựng phần mềm" một cách bài bản.

---

_Built with ❤️ for the AgentsicSE community._
