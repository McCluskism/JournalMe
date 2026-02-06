from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_booklet(filename, prompts):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Define starting position
    x_offset = 50
    y_offset = height - 50
    line_height = 20
    
    for prompt in prompts:
        c.drawString(x_offset, y_offset, prompt)
        y_offset -= line_height  # Move down for the next prompt
        
        # Add empty space for notes
        c.rect(x_offset, y_offset - 10, 500, 100, fill=0)
        y_offset -= 100  # Move down past the empty space

    c.save()  

if __name__ == '__main__':
    prompts = [
        'What did I learn today?',
        'What challenges did I face?',
        'What am I grateful for?',
        'What is my goal for tomorrow?'
    ]
    create_booklet('journal_booklet.pdf', prompts)