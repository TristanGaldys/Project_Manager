import tkinter as tk

def create_rounded_rectangle(canvas, x1, y1, x2, y2, corner_radius, **kwargs):
    # Draw the main rectangle
    canvas.create_polygon(
        x1 + corner_radius, y1,
        x1 + corner_radius, y1,
        x2 - corner_radius, y1,
        x2 - corner_radius, y1,
        x2, y1,
        x2, y1 + corner_radius,
        x2, y1 + corner_radius,
        x2, y2 - corner_radius,
        x2, y2 - corner_radius,
        x2, y2,
        x2 - corner_radius, y2,
        x2 - corner_radius, y2,
        x1 + corner_radius, y2,
        x1 + corner_radius, y2,
        x1, y2,
        x1, y2 - corner_radius,
        x1, y2 - corner_radius,
        x1, y1 + corner_radius,
        x1, y1 + corner_radius,
        x1, y1,
        x1 + corner_radius, y1,
        smooth=True,
        **kwargs
    )

def on_item_click(event, item):
    """Handle click on a canvas item"""
    print(f"You clicked on: {item['name']}")

root = tk.Tk()
root.title("Custom List on Canvas")

canvas = tk.Canvas(root, bg='white', width=400, height=600)
canvas.pack(pady=20, padx=20)

# Sample data
data = [
    {"name": "John Doe", "age": "25", "role": "Engineer"},
    {"name": "Jane Smith", "age": "30", "role": "Manager"},
    {"name": "Alice", "age": "28", "role": "Designer"}
]

# Loop through data and create items on canvas
y_position = 20  # Starting y-position
height_of_item = 60  # Height of each item
spacing = 10  # Vertical spacing between items

for index, item in enumerate(data):
    tag_name = f"item_{index}"
    
    # Draw a rounded rectangle
    create_rounded_rectangle(canvas, 10, y_position, 390, y_position + height_of_item, 10, fill="#37465B", tag=tag_name)
    
    # Bind click event to the rectangle
    canvas.tag_bind(tag_name, "<Button-1>", lambda event, item=item: on_item_click(event, item))
    
    # Draw name (bigger font, left)
    canvas.create_text(
        20, y_position + height_of_item/2, 
        text=item["name"], 
        font=("Arial", 16), 
        anchor='w'
    )
    
    # Draw age (smaller font, right)
    canvas.create_text(
        380, y_position + 15, 
        text=item["age"], 
        font=("Arial", 12, "italic"), 
        anchor='e'
    )
    
    # Draw role (smaller font, right, below age)
    canvas.create_text(
        380, y_position + height_of_item - 15, 
        text=item["role"], 
        font=("Arial", 12), 
        anchor='e'
    )
    
    # Increment the y_position for next item
    y_position += height_of_item + spacing

root.mainloop()
