import pywinauto
from pywinauto.application import Application
from pywinauto import mouse
from pywinauto import keyboard
import time
from PIL import ImageGrab,Image
from pywinauto.keyboard import send_keys

def mission_planner(lg1,la1,lg2,la2,lg3,la3,lg4,la4):
    def Process_image():
        im = Image.open('img.png')
        x1, y1, x2, y2 = 0, 90, 1920, 975
        cropped = im.crop((x1, y1, x2, y2))
        cropped.save("img.png")
    APP = Application(backend='uia').connect(title='Mission Planner 1.3.77 build 1.3.8110.38294',timeout=100)
    DLG = APP['Mission Planner 1.3.77 build 1.3.8110.38294']
    DLG.print_control_identifiers()
    SIMULATION = DLG.child_window(title="SIMULATION", control_type="Button").wrapper_object()
    SIMULATION.click_input()
    PLANE = DLG.child_window(title="Plane Swarm - Multilink", auto_id="but_swarmplane", control_type="Button").wrapper_object()
    PLANE.click_input()
    PLANE.click_input()
    pywinauto.mouse.double_click(button='left',coords=(999,569))
    time.sleep(40)
    PLAN = DLG.child_window(title="PLAN", control_type="Button").wrapper_object()
    time.sleep(1)
    PLAN.click_input()
    PLAN.click_input()
    PLAN.click_input()
    ADD_BELOW = DLG.child_window(title="Add Below", auto_id="BUT_Add", control_type="Button").wrapper_object()
    ADD_BELOW.click_input()
    LAT = DLG.child_window(title="Lat Row 0", control_type="Edit").wrapper_object()
    LAT.click_input()
    LAT.type_keys(str(la1),with_spaces='True')
    LAT.click_input()
    LONG = DLG.child_window(title="Long Row 0", control_type="Edit").wrapper_object()
    LONG.click_input()
    LONG.type_keys(str(lg1),with_spaces='True')
    ALT = DLG.child_window(title="Alt Row 0", control_type="Edit").wrapper_object()
    ALT.click_input()
    ALT.type_keys('100',with_spaces='True')
    ADD_BELOW.click_input()
    LAT1 = DLG.child_window(title="Lat Row 1", control_type="Edit").wrapper_object()
    LAT1.click_input()
    LAT1.type_keys(str(la2),with_spaces='True')
    LONG1 = DLG.child_window(title="Long Row 1", control_type="Edit").wrapper_object()
    LONG1.click_input()
    LONG1.type_keys(str(lg2),with_spaces='True')
    ALT1 = DLG.child_window(title="Alt Row 1", control_type="Edit").wrapper_object()
    ALT1.click_input()
    ALT1.type_keys('100',with_spaces='True')
    ADD_BELOW.click_input()
    LAT2 = DLG.child_window(title="Lat Row 2", control_type="Edit").wrapper_object()
    LAT2.click_input()
    LAT2.type_keys(str(la3),with_spaces='True')
    LONG2 = DLG.child_window(title="Long Row 2", control_type="Edit").wrapper_object()
    LONG2.click_input()
    LONG2.type_keys(str(lg3),with_spaces='True')
    ALT2 = DLG.child_window(title="Alt Row 2", control_type="Edit").wrapper_object()
    ALT2.click_input()
    ALT2.type_keys('100',with_spaces='True')
    ADD_BELOW.click_input()
    LAT3 = DLG.child_window(title="Lat Row 3", control_type="Edit").wrapper_object()
    LAT3.click_input()
    LAT3.type_keys(str(la4),with_spaces='True')
    LONG3 = DLG.child_window(title="Long Row 3", control_type="Edit").wrapper_object()
    LONG3.click_input()
    LONG3.type_keys(str(lg4),with_spaces='True')
    ALT3 = DLG.child_window(title="Alt Row 3", control_type="Edit").wrapper_object()
    ALT3.click_input()
    ALT3.type_keys('100',with_spaces='True')
    COMMAND = DLG.child_window(title="Command Row 0", control_type="ComboBox").wrapper_object()
    COMMAND.click_input()
    COMMAND.click_input()
    COMMAND.click_input()
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    COMMAND = DLG.child_window(title="Command Row 1", control_type="ComboBox").wrapper_object()
    COMMAND.click_input()
    COMMAND.click_input()
    COMMAND.click_input()
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    send_keys('{DOWN}')
    pywinauto.mouse.click(button='left',coords=(214,534))
    WRIGHT = DLG.child_window(title="Write", auto_id="BUT_write", control_type="Button").wrapper_object()
    WRIGHT.click_input()
    DATA = DLG.child_window(title="DATA", control_type="Button").wrapper_object()
    DATA.click_input()
    DATA.click_input()
    ACTIONS = DLG.child_window(title="Actions", control_type="TabItem").wrapper_object()
    ACTIONS.click_input()
    ARM = DLG.child_window(title="Arm/ Disarm", auto_id="BUT_ARM", control_type="Button").wrapper_object()
    ARM.click_input()
    SET_MODE = DLG.child_window(title="Set Mode", auto_id="BUT_setmode", control_type="Button").wrapper_object()
    SET_MODE.click_input()
    pywinauto.keyboard.send_keys('^f')
    t = Application(backend='uia').connect(title='temp',timeout=100)
    Temp = t['temp']
    THREE_D = Temp.child_window(title="3D Map", auto_id="but_3dmap", control_type="Button").wrapper_object()
    THREE_D.click_input()
    time.sleep(5)
    send_keys('%{SPACE}')
    send_keys('x')
    time.sleep(10)
    for image in range(20):
        time.sleep(2)
        screen_shot = ImageGrab.grab()
        screen_shot.save('img.png')
        Process_image()
#test_case
mission_planner(35,35,35,35,35,35,35,35)
