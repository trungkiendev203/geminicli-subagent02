# Geminicli-subagent02

Ví dụ về cách tạo một GeminiCLI subagent dành cho AI Agents, sẵn sàng cho giai đoạn tiếp theo là **AgentsicSE**.

## Giới thiệu

Repository này chứa một ví dụ mẫu (template) về việc xây dựng một subagent sử dụng GeminiCLI. Đây là bước đệm quan trọng để tiến tới hệ thống AI Agents phức tạp hơn, cụ thể là hướng tới kỷ nguyên **AgentsicSE** (Agentic Software Engineering).

## Tính năng

- Cấu trúc thư mục chuẩn cho một subagent (.agent config).
- Các ví dụ về workflows cho quá trình phát triển phần mềm tự động.
- Script bổ trợ giúp Agent tự phân tích dự án.

## Cấu trúc Repository

```text
geminicli-subagent02/
├── .agent/                 # Cấu hình dành riêng cho Agent
│   ├── instructions.md     # Persona và quy tắc của subagent
│   └── workflows/          # Các quy trình tự động hóa (Workflows)
│       └── refactor.md     # Ví dụ workflow về refactor code
├── scripts/                # Các công cụ/scripts mà Agent có thể gọi
│   └── analyze.py          # Script phân tích cấu trúc dự án mẫu
└── README.md
```

## Cách sử dụng mẫu

Mỗi subagent được thiết kế để "hiểu" thư mục `.agent`. Khi bạn nạp subagent này vào GeminiCLI:

1. Nó sẽ đọc `instructions.md` để biết vai trò của mình.
2. Nó có thể thực thi các quy trình trong `workflows/` bằng cách làm theo từng bước được định nghĩa.
3. Nó có thể chạy các script trong `scripts/` để thu thập dữ liệu về codebase.

## Mục tiêu

Phát triển các công cụ hỗ trợ lập trình viên (AI-assisted coding) thông qua việc module hóa các tác vụ thành các subagents chuyên biệt.
