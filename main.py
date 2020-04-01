import os
from Script.capture import function_capture

current_dir = os.path.dirname(os.path.realpath(__file__))
new_dir = (current_dir+'/Data/data.xlsx')
function_capture=function_capture(new_dir)