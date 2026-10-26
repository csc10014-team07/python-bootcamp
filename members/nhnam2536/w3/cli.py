from datetime import date, datetime
from pathlib import Path
import sys
import argparse


def main() -> None:
  parser = argparse.ArgumentParser(description="Task CLI Tool")
  parser.add_argument("file", type=str, help="Path to tasks CSV file")
  parser.add_argument(
      "--hours", type=float, required=True, help="Available hours"
  )
  parser.add_argument(
      "--today",
      type=str,
      default=None,
      help="Reference date (YYYY-MM-DD), default is today",
  )

  args = parser.parse_args()

  # check existing file
  file_path = Path(args.file)
  if not file_path.is_file():
    print(
        f"Error: File '{args.file}' does not exist.",
        file=sys.stderr,
    )
    sys.exit(1)

  if args.today:
    try:
      today_date = datetime.strptime(args.today, "%Y-%m-%d").date()
    except ValueError:
      print(
          "Error: --today must be in YYYY-MM-DD format.",
          file=sys.stderr,
      )
      sys.exit(1)
  else:
    today_date = date.today()

  print(f"Running tasks for date: {today_date} with {args.hours} hours...")


if __name__ == "__main__":
  main()