import os
import sys

def analyze_complexity(directory):
    """
    Một script mẫu giúp agent phân tích độ phức tạp của thư mục.
    AgentsicSE: Agent có thể tự gọi script này để lấy thông tin.
    """
    print(f"--- Đang phân tích thư mục: {directory} ---")
    files_count = 0
    dirs_count = 0
    
    for root, dirs, files in os.walk(directory):
        if ".git" in dirs:
            dirs.remove(".git")
        if ".agent" in dirs:
            dirs.remove(".agent")
            
        files_count += len(files)
        dirs_count += len(dirs)
        
    print(f"Tổng số tệp tin: {files_count}")
    print(f"Tổng số thư mục: {dirs_count}")
    print("Trạng thái: Sẵn sàng cho quá trình Agentic SE.")

if __name__ == "__main__":
    analyze_complexity(os.getcwd())
