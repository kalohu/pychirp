class Layout(object):
    
    def calculate_child_position(self, parent, child):
        child_x = parent['x']
        child_x += (parent['width'] - child['width']) / 2 if parent['width'] > child['width'] else 20

        child_y = parent['y']
        child_y += (parent['height'] - child['height']) / 2 if parent['height'] > child['height'] else 20

        return child_x, child_y
