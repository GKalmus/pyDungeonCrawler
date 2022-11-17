class fg:
      BLACK = "\u001b[30m"
      RED = "\u001b[31m"
      GREEN = "\u001b[32m"
      YELLOW = "\u001b[33m"
      BLUE = "\u001b[34m"
      MAGENTA = "\u001b[35m"
      CYAN = "\u001b[36m"
      WHITE = "\u001b[37m"

      def rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"

class bg:
      BLACK = "\u001b[40m"
      RED = "\u001b[41m"
      GREEN = "\u001b[42m"
      YELLOW = "\u001b[43m"
      BLUE = "\u001b[44m"
      MAGENTA = "\u001b[45m"
      CYAN = "\u001b[46m"
      WHITE = "\u001b[47m"

      def rgb(r, g, b): return f"\u001b[48;2;{r};{g};{b}m"

class util:
      RESET = "\u001b[0m"
      BOLD = "\u001b[1m"
      UNDERLINE = "\u001b[4m"
      REVERSE = "\u001b[7m"

      CLEAR = "\u001b[2J"
      CLEARLINE = "\u001b[2K"

      UP = "\u001b[1A"
      DOWN = "\u001b[1B"
      RIGHT = "\u001b[1C"
      LEFT = "\u001b[1D"

      NEXTLINE = "\u001b[1E"
      PREVLINE = "\u001b[1F"

      TOP = "\u001b[0;0H"

      def to(x, y):
            return f"\u001b[{y};{x}H"

      def write(text="\n"):
            stdout.write(text)
            stdout.flush()

      def writew(text="\n", wait=0.5):
            for char in text:
                  stdout.write(char)
                  stdout.flush()
                  sleep(wait)

      def read(begin=""):
            text = ""

            stdout.write(begin)
            stdout.flush()

            while True:
                  char = ord(stdin.read(1))
                  if char == 3: return
                  elif char in (10, 13): return text
                  else: text += chr(char)

      def readw(begin="", wait=0.5):
            text = ""

            for char in begin:
                  stdout.write(char)
                  stdout.flush()
                  sleep(wait)

            while True:
                  char = ord(stdin.read(1))
                  
                  if char == 3: return
                  elif char in (10, 13): return text
                  else: text += chr(char)