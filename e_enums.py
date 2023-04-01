# Author : Jonathan
# Created: June-22-2020

#TO Use COLORS.BLUE.value (provides (255,0,0)
class COLORS(Enum):
    # TODO: Oct-21-2020, remove this enum and use COLORS_e
    RED = (0, 0, 255) #BGR
    BLUE = (255, 0, 0) #BGR
    BEIGE = (220, 245, 245) 
    GREEN = (0, 255, 0)  # BGR
    YELLOW = (0, 255, 255)
    WHITE = (255, 255, 255)
    ORANGE = (0, 165, 255)
    PURPLE = (255, 0, 127)
    VIOLET = (238, 130, 238)
    PINK = (255, 0, 255)
    ROSE = (127, 0, 225)
    BLACK = (0, 0, 0)
    GRAY = (128,128,128)
    GRAY2 = (105, 105, 105)
    DARKBLUE = (153, 51, 0)
    DARKBLUE2 = (107, 0, 0)
    DARKRED = (3,3,128)
    DARKORANGE = (28, 71, 102) #BROWN
    LIGHTGREEN = (96,236,80)
    LIGHTBLUE = (255,255,0)

class ConsoleColor:
    '''
    ConsoleColor - Used for changing the console text color
    ref:
        1. https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
        2. https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
    '''
    # TODO: Low, JW, Dec-23-2020

    HEADER = '\033[95m'  # Light Purple
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Reversed  ="\u001b[7m"
    ENDC = '\033[0m'

    # Block:
    INFO = '\033[94m'     #Light Blue
    WARNING = '\033[93m'  # Yellow
    ERROR   = '\033[91m'  # Red
    FAIL = '\033[91m'     # Red

    # Block: color
    PURPLE = '\033[95m' #Light Purple
    OKBLUE = '\033[94m' #Light Blue
    LIGHTBLUE = '\033[94m' #Light Blue
    OKCYAN = '\033[96m' #Cyan Blue
    OKGREEN = '\033[92m' #Yellow Green
    WARNING = '\033[93m' #Yellow
    YELLOW = '\033[93m' #Yellow
    FAIL = '\033[91m' #Red
    RED = '\033[91m' #Red
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m' 
    

class COLORS_e():
    RED = (0, 0, 255) #BGR
    BLUE = (255, 0, 0) #BGR
    BEIGE = (220, 245, 245)
    GREEN = (0, 255, 0)  # BGR
    YELLOW = (0, 255, 255)
    WHITE = (255, 255, 255)
    ORANGE = (0, 165, 255)
    PURPLE = (255, 0, 127)
    VIOLET = (238, 130, 238)
    PINK = (255, 0, 255)
    ROSE = (127, 0, 225)
    BLACK = (0, 0, 0)
    GRAY = (128,128,128)
    GRAY2 = (105, 105, 105)
    REDORANGE = (0, 89, 255)
    DARKBLUE = (153, 51, 0)
    DARKBLUE2 = (107, 0, 0)
    DARKRED = (3,3,128)
    DARKORANGE = (28, 71, 102) #BROWN
    DARKYELLOW = (0, 217, 255)
    DARKGREEN = (0,128,0)
    LIGHTGREEN = (96,236,80)
    LIGHTBLUE = (255,255,0)



def print_color(input, color=ConsoleColor.WARNING):
    print(f"{color}{input}{ConsoleColor.ENDC}")

