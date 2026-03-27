# pdf-merge

A lightweight Python utility to merge multiple PDF files with precise, human-friendly page range control.

---

## Usage

Run the script from your terminal by passing the input files (with optional page ranges) followed by the desired output name.

```bash
python pdf-fuse.py <file1:start-end> <file2:start-end> ...  <fileN:start-end> <output.pdf>
```

### Page Range Syntax
Ranges use **1-based indexing** (human counting). 
* `file.pdf:1-3` — Extracts pages 1, 2, and 3.
* `file.pdf` — Appends the entire document.

### Examples
* **Basic Merge:** python pdf-fuse.py input1.pdf input2.pdf output.pdf
* **Specific Pages:** python pdf-fuse.py input1.pdf:1-3 input2.pdf:5-10 output.pdf
* **Mixed Input:** python pdf-fuse.py input1.pdf:1-2 input2.pdf output.pdf

## Requirements
1. **Python 3.6+**
2. **pypdf library:** `pip install pypdf`

## Error Handling
The script will safely skip missing files or invalid file types. If a requested page range exceeds the actual page count of a document, the script will alert you and exit to prevent a corrupted output.
