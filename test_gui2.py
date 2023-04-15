from graphics import *
import pyautogui
import tkinter.filedialog as fd
import shutil
import os
import platform

# Window Creation
#----------------
WINDOW_WIDTH, WINDOW_HEIGHT = pyautogui.size()
WINDOW_WIDTH, WINDOW_HEIGHT = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
recording_on = False
circle1 = Circle(Point(WINDOW_WIDTH*(6/8), WINDOW_HEIGHT*(2/5)), 120)
circle2 = Circle(Point(WINDOW_WIDTH*(6/8), WINDOW_HEIGHT*(2/5)), 110)
circle3 = Circle(Point(WINDOW_WIDTH*(6/8), WINDOW_HEIGHT*(2/5)), 100)
win = GraphWin("[TBD]", WINDOW_WIDTH, WINDOW_HEIGHT)
setbackground = win.setBackground("black")
#----------------

def buttons():
    circle1.setFill("white")
    circle2.setFill("black")
    circle3.setFill("red")
    rect = Rectangle(Point(circle1.getCenter().getX()-120, circle1.getCenter().getY()-120), Point(circle1.getCenter().getX()+120, circle1.getCenter().getY()+120))
    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)


def inside(point, rectangle):
    """ Is point inside rectangle? """
    lower_left = rectangle.getP1()  # assume p1 is lower_left (lower left)
    upper_right = rectangle.getP2()  # assume p2 is upper_right(upper right)
    return lower_left.getX() < point.getX() < upper_right.getX() and lower_left.getY() < point.getY() < upper_right.getY()

def open_file():
    """Open a file for editing"""
    try:
        filepath = fd.askopenfilename()
        save_file(filepath)
    except:
        pass

def draw_button(win, pos, size, text):
    """Draw a button on the window"""
    rect = Rectangle(Point(pos[0], pos[1]), Point(pos[0]+size[0], pos[1]+size[1]))
    rect.setFill('white')
    rect.draw(win)
    label = Text(Point(pos[0]+size[0]//2, pos[1]+size[1]//2), text)
    label.draw(win)
    return rect

def save_file(filepath):
    """Save a file"""
    SLASH = get_slash()
    try:
        filename = os.path.basename(filepath)
        normalized_path = os.path.normpath(filepath)
        shutil.copy(normalized_path, f"audio_files{SLASH}{filename}")
    except:
        print("this is bad")

def get_slash():
    """Get the slash for the operating system"""
    op_sys = platform.system()
    if op_sys == 'Darwin' or op_sys == 'Linux': # Mac or Linux
        SLASH = r'/'
    else:
        SLASH = fr'\'' # Windows
    return SLASH

button_pos = (75, 75)
button_size = (300, 50)
button_text = 'Select File'
button = draw_button(win, button_pos, button_size, button_text)

buttons()

line = Rectangle(Point((WINDOW_WIDTH / 2)-5, WINDOW_HEIGHT), Point((WINDOW_WIDTH / 2)+5, 0))
line.draw(win).setFill("gray")


while True:
    try:
        click_point = win.getMouse()
        if click_point is None:  # so we can substitute checkMouse() for getMouse()
            break
        elif inside(click_point, Rectangle(Point(circle1.getCenter().getX()-120, circle1.getCenter().getY()-120), Point(circle1.getCenter().getX()+120, circle1.getCenter().getY()+120))):
            if recording_on == False:
                recording_on = True
                circle3.setFill("green")
            else:
                recording_on = False
                circle3.setFill("red")
        elif button.getP1().getX() <= click_point.getX() <= button.getP2().getX() and \
            button.getP1().getY() <= click_point.getY() <= button.getP2().getY():
            open_file()
        else:
            pass
    except:
        pass



win.close()


