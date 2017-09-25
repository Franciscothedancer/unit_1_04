

import ui

def calculate_touch_up_inside(sender):
    # calculate circumference
    
    # constants
    PI = 3.14
    
    # input
    radius = int(view['radius_textbox'].text)
    
    # process
    circumference = 2 * PI * radius
    
    # output
    view['answer_label'].text = 'The circumference is: ' + str(circumference) + ' cm'

view = ui.load_view()
view.present('full_screen')
