import argparse
from datetime import date
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Study Planner Command Line Tool")
    parser.add_argument("file", type=str, help="Đường dẫn đến file CSV chứa danh sách tác vụ (tasks.csv)")
    parser.add_argument("--hours", type=float, required=True, help="Số giờ rảnh có sẵn")
    parser.add_argument("--today", type=str, default=str(date.today()), help="Ngày hiện tại theo định dạng YYYY-MM-DD")
    
    args = parser.parse_args()
    
    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Lỗi: Không tìm thấy file '{args.file}'.", file=sys.stderr)
        sys.exit(1)
        
    try:
        today_date = date.fromisoformat(args.today)
    except ValueError:
        print(f"Lỗi: Định dạng ngày --today không hợp lệ: '{args.today}'. Sử dụng YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Đang xử lý file {file_path.name} với mốc ngày {today_date} và {args.hours} giờ khả dụng...")

if __name__ == "__main__":
    main()