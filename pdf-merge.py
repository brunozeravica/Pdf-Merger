import os
from pathlib import Path
from pypdf import PdfReader, PdfWriter, PageRange
import sys

def main():

    if len(sys.argv) < 3:
        print_help()
        sys.exit(1)

    # All arguments except last one are inputs
    inputs = sys.argv[1:-1]
    # Last argument is the output
    output = sys.argv[-1]

    merge_pdfs(inputs, output)


def merge_pdfs(input_paths, output_path):
    writer = PdfWriter()

    merge_count = 0
    for path in input_paths:

        # Determine page range if given
        page_range = None
        if ":" in path:
            path, range_str = path.split(":", 1)
            try:
                parts = range_str.split("-")
                if len(parts) == 2:
                    start, end = int(parts[0]), int(parts[1])
                    page_range = (start - 1, end)

                else:
                    print(f"Invalid range format for {path}. Use start-end (e.g. 1-3).")

            except ValueError:
                print(f"Non-numeric range provided for {path}. Skipping range.")

        if not os.path.exists(path):
            print(f"Skipping {path}: File not found")
            continue

        if not Path(path.lower()).suffix == ".pdf":
            print(f"Skipping {path}: Invalid file type")
            continue

        print(f"Adding: {path}")
        writer.append(path, page_range)
        merge_count += 1

    if merge_count == 0:
        print("No valid files were provided, not generating output")
        return

    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Merged {len(input_paths)} PDFs into: {output_path}")


def print_help():
    help_text = """
pdf-merge | A precise PDF merging tool.

Usage:
  python pdf-merge.py <file1:start-end> <file2:start-end> ...  <fileN:start-end> <output.pdf>

Examples:
  Full Files:    python pdf-merge.py input1.pdf input2.pdf output.pdf
  Specific Pages: python pdf-merge.py input1.pdf:1-3 input2.pdf:5-10 output.pdf
  Mixed:         python pdf-merge.py input1.pdf:1-2 input2.pdf output.pdf

Note: Page ranges are 1-indexed (human counting). 1-3 includes page 1, 2, and 3.
    """
    print(help_text)


if __name__ == "__main__":
    main()
