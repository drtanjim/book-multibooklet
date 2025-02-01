Here's the updated interactive GitHub description with a mention that it is for a simplex printer:

---

# PDF Booklet Generator 📚

Create print-ready booklets from PDF files using Python and MuPDF. This script splits your PDF into front and back faces for printing, with pages organized in a way that makes folding and binding easy. Blank pages are added as needed to ensure booklet completion. **This solution is designed for simplex printers**, which print on one side of the paper.

## Features ✨
- **Dynamic Booklet Sizing:** Handles any total number of pages, with configurable booklet size.
- **Handles Blanks:** Automatically inserts blank pages where required to ensure proper booklet folding.
- **Front and Back Faces:** Generates separate PDF files for front and back faces.
- **A4 Landscape:** Arranges two pages on each A4 landscape sheet, perfect for booklet printing.

## Requirements 🚀
- Python 3.6+
- MuPDF (PyMuPDF)

## Installation 🛠️
Install the required library using pip:
```bash
pip install pymupdf
```

## Usage 📄
Edit the `input_pdf`, `output_front_pdf`, and `output_back_pdf` variables as needed.

```python
import fitz

def generate_booklet_pattern(total_pages, booklet_size=20):
    # Your code here

def create_booklet_pdf(input_pdf, output_front_pdf, output_back_pdf, booklet_size=20):
    # Your code here

# Example usage
input_pdf = "input.pdf"  # Replace with your input PDF file path
output_front_pdf = "front_face.pdf"
output_back_pdf = "back_face.pdf"
create_booklet_pdf(input_pdf, output_front_pdf, output_back_pdf)
```

## How It Works ⚙️
1. **Generate Booklet Pattern:** Calculates the order of pages for the front and back faces.
2. **Process PDF:** Loads the input PDF and splits it into front and back pages.
3. **Combine Pages:** Creates new PDF pages in A4 landscape format, placing two original pages per sheet.
4. **Insert Blanks:** Adds blank pages where needed to complete each booklet.

## Example 🖼️
Here's a quick example of how the pages are laid out:

```
Front Face Order:  [8, 1, 2, 7, 6, 3, 4, 5, 'Blank', 'Blank', 'Booklet Break', 'Booklet Break']
Back Face Order:  [7, 2, 1, 8, 5, 4, 3, 6, 'Blank', 'Blank', 'Booklet Break', 'Booklet Break']
```

## Contributing 🌟
Feel free to fork the repository and make improvements. Pull requests are always welcome!

## License 📄
This project is licensed under the MIT License.

---

Feel free to customize and expand upon this description as you see fit. Let me know if there's anything else I can help you with!
