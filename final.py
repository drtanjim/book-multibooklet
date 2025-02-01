import fitz

def generate_booklet_pattern(total_pages, booklet_size=20):
    front_face = []
    back_face = []
    remaining_pages = total_pages
    start_page = 1

    while remaining_pages > 0:
        current_booklet_size = min(booklet_size, remaining_pages)
        adjusted_pages = current_booklet_size
        while adjusted_pages % 4 != 0:
            adjusted_pages += 1

        pages = list(range(start_page, start_page + current_booklet_size)) + ['Blank'] * (adjusted_pages - current_booklet_size)

        for i in range(adjusted_pages // 4):
            front_face.append(pages[-(2 * i + 1)])  # Front face order
            front_face.append(pages[2 * i])

            back_face.append(pages[2 * i + 1])  # Back face order
            back_face.append(pages[-(2 * i + 2)])

        front_face.append("Booklet Break")
        front_face.append("Booklet Break")
        back_face.append("Booklet Break")
        back_face.append("Booklet Break")

        remaining_pages -= current_booklet_size
        start_page += current_booklet_size

    return front_face, back_face

def create_booklet_pdf(input_pdf, output_front_pdf, output_back_pdf, booklet_size=20):
    input_document = fitz.open(input_pdf)
    total_pages = len(input_document)
    front_face, back_face = generate_booklet_pattern(total_pages, booklet_size)

    def add_pages_to_document(document, page_num1, page_num2):
        page = document.new_page(width=841.68, height=595.44)  # Landscape A4 dimensions in points
        if page_num1 != 'Blank':
            page1 = input_document.load_page(page_num1 - 1)
            page.show_pdf_page(fitz.Rect(0, 0, 421.68, 595.44), input_document, page1.number)
        if page_num2 != 'Blank':
            page2 = input_document.load_page(page_num2 - 1)
            page.show_pdf_page(fitz.Rect(421.68, 0, 841.68, 595.44), input_document, page2.number)

    front_document = fitz.open()
    back_document = fitz.open()

    for i in range(0, len(front_face), 2):
        page_num1 = front_face[i]
        page_num2 = front_face[i + 1] if i + 1 < len(front_face) else 'Blank'
        if page_num1 == "Booklet Break":
            continue
        add_pages_to_document(front_document, page_num1, page_num2)

    for i in range(0, len(back_face), 2):
        page_num1 = back_face[i]
        page_num2 = back_face[i + 1] if i + 1 < len(back_face) else 'Blank'
        if page_num1 == "Booklet Break":
            continue
        add_pages_to_document(back_document, page_num1, page_num2)

    front_document.save(output_front_pdf)
    back_document.save(output_back_pdf)

# Example usage
input_pdf = "input.pdf"  # Replace with your input PDF file path
output_front_pdf = "front_face.pdf"
output_back_pdf = "back_face.pdf"
create_booklet_pdf(input_pdf, output_front_pdf, output_back_pdf)
