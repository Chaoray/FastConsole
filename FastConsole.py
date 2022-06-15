import win32console
import win32con
from win32api import GetSystemMetrics

class Console:
    def __init__(self, width=120, height=30):
        '''
        Create new Console instance with specified width and height.\n
        The specified width and height cannot be less than the width and height of the console screen buffer's window. \n
        The specified dimensions also cannot be less than the minimum size allowed by the system. \n
        Use getMinConsoleSize(). \n

        Warning: Don't use Input() function after Console attached.
        '''
        self.hConsoleOutput = win32console.CreateConsoleScreenBuffer(DesiredAccess=win32con.GENERIC_READ | win32con.GENERIC_WRITE, ShareMode=0, SecurityAttributes=None, Flags=1)
        self.stdHandle = win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)

        self.width = width
        self.height = height

        self.hConsoleOutput.SetConsoleScreenBufferSize(win32console.PyCOORDType(self.width, self.height))
        
    def attach(self):
        '''
        Attach to current console
        '''
        self.hConsoleOutput.SetConsoleActiveScreenBuffer()
        self.hConsoleOutput.SetConsoleScreenBufferSize(win32console.PyCOORDType(self.width, self.height))

    def detach(self):
        '''
        Detach from current console
        '''
        self.hConsoleOutput.Detach()
        self.stdHandle.SetConsoleActiveScreenBuffer()

    def close(self):
        '''
        Close console handle
        '''
        self.hConsoleOutput.Close()

    def writeCursor(self, buffer=''):
        '''
        Writes a string of characters at current cursor position. \n
        Return True if all characters were written successfully.
        '''
        nLength = self.hConsoleOutput.WriteConsole(buffer)

        return nLength == len(buffer)

    def write(self, buffer='', x=0, y=0):
        '''
        Writes a string of characters at a specified position. \n
        Return True if all characters were written successfully.
        '''
        nLength = self.hConsoleOutput.WriteConsoleOutputCharacter(buffer, win32console.PyCOORDType(x, y))

        return nLength == len(buffer)

    def clear(self):
        '''
        Fill the entire buffer with spaces
        '''
        self.hConsoleOutput.FillConsoleOutputCharacter(' ', self.width * self.height, win32console.PyCOORDType(0, 0))

    def pointTo(self, x=0, y=0):
        '''
        The coordinates are the column and row of a screen buffer character cell. \n
        The coordinates must be within the boundaries of the console screen buffer.
        '''
        self.hConsoleOutput.SetConsoleCursorPosition(win32console.PyCOORDType(x, y))

    def setCursorVisibility(self, isShow=True):
        self.hConsoleOutput.SetConsoleCursorInfo(1, isShow)

    def getMinConsoleSize(self):
        '''
        Returns the minimum (width, height) of console buffer.
        '''
        return (GetSystemMetrics(28), GetSystemMetrics(29))

    def refer(self, handle):
        '''
        Combine multi console instances. \n
        Get handle from Console.hConsoleOutput
        '''
        self.hConsoleOutput.Detach()
        self.hConsoleOutput.Close()

        self.hConsoleOutput = handle
        
        size = handle.GetConsoleScreenBufferInfo()['Size']

        self.width = size.X
        self.height = size.Y

    def __del__(self):
        self.detach()
        self.close()
