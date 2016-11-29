import sys
from forms.user_form import *


if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("At least one argument is required")
	else:
		if sys.argv[1] == 'run':
			win = make_windows()
			set_select()
			win.mainloop()