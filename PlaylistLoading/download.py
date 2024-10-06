import fitz  # PyMuPDF

# Open the PDF file
pdf_path = '/Downloads/Python_Book.pdf'
doc = fitz.open(pdf_path)

# Directory to save the Python files
output_dir = '/Downloads/Progrmas'

import os

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to extract code blocks and save them as .py files
def extract_code_blocks(page_text, page_num):
    code_blocks = []
    in_code_block = False
    code_block = []
    
    for line in page_text.splitlines():
        if line.strip().startswith(">>>") or line.strip().startswith("Example:"):
            in_code_block = True
            code_block = [line.strip().replace(">>>", "").strip()]
        elif in_code_block and (line.strip() or line.strip() == ""):
            code_block.append(line.strip())
        elif in_code_block:
            in_code_block = False
            if code_block:
                code_blocks.append("\n".join(code_block))
    
    # Save each code block as a separate file
    for i, block in enumerate(code_blocks):
        file_name = f"page_{page_num + 1}_example_{i + 1}.py"
        with open(os.path.join(output_dir, file_name), "w") as f:
            f.write(block)

# Iterate through the pages and extract code
for page_num in range(len(doc)):
    page = doc[page_num]
    page_text = page.get_text()
    extract_code_blocks(page_text, page_num)

output_dir
