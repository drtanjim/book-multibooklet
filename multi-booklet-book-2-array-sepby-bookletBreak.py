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

# Example usage
total_pages = 85  # Change as needed
front, back = generate_booklet_pattern(total_pages)
print("Front Face Order:", front)
print("Back Face Order:", back)
