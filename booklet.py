def generate_booklet_pattern(total_pages):
    # Ensure total pages is a multiple of 4 by adding blank pages ('Blank')
    adjusted_pages = total_pages
    while adjusted_pages % 4 != 0:
        adjusted_pages += 1
    
    pages = list(range(1, total_pages + 1)) + ['Blank'] * (adjusted_pages - total_pages)
    front_face = []
    back_face = []
    
    for i in range(adjusted_pages // 4):
        front_face.append(pages[-(2 * i + 1)])  # Front face order
        front_face.append(pages[2 * i])
        
        back_face.append(pages[2 * i + 1])  # Back face order
        back_face.append(pages[-(2 * i + 2)])
    
    return front_face, back_face

# Example usage
total_pages = 21  # Change as needed
front, back = generate_booklet_pattern(total_pages)
print("Front Face Order:", front)
print("Back Face Order:", back)
