
# 📄 PDF Search Tool with Python

A small Python script for automatically searching through PDF files in specific folders for defined keywords.  
Perfect for situations where you have many local PDFs and need to quickly find which ones contain relevant content.

## 🚀 Features

- 🔍 **Path selection**: Choose from predefined search paths  
- 📂 **Recursive folder search**: Includes all subfolders  
- 📝 **Full-text search** in PDFs (single or double keyword search)  
- 📊 **Simple result output** in the terminal  
- ⚠️ Error handling for unreadable PDFs

## 📦 Requirements

- **Python 3.x**  
- Libraries:
  ```bash
  pip install PyPDF2
  ```

## ⚙️ Installation & Usage

1. **Clone the repository or download the script**  
2. **Adjust the search paths**  
   ```python
   path1 = 'YOUR\\PATH\\HERE'
   path2 = 'YOUR\\PATH\\HERE'
   path3 = 'YOUR\\PATH\\HERE'
   ```
3. **Run the script**  
   ```bash
   python pdf_search.py
   ```
4. **Select a path**  
   The terminal will prompt you to choose one of the three preset search paths.
5. **Enter keyword(s)**  
   - Only the first keyword → single keyword search  
   - Two keywords → both must appear in the document
6. **View the results**  
   The terminal will list the found files with their full paths.

## 💡 Example Run

```text
Which path should be selected? (1: PATH1, 2: PATH2, 3: PATH3): 1
Keyword 1: invoice
Keyword 2: 2023

Searching for: ['invoice', '2023'] Number of terms: 2

Search results:

C:\Documents\Projects\Finance\invoice_april_2023.pdf
C:\Documents\Invoices\Clients\invoice_may_2023.pdf
```

## 🛠️ Possible Improvements

- 📈 Progress indicator for large numbers of files  
- 🗂 Export results to CSV or HTML  
- 🧠 Regular expression support for more complex searches  
- 🖥 GUI version for users unfamiliar with the command line
```
