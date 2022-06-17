print("What is the Python interpreter?")
print("What is interactive mode?")
print("How do you utilize argument passing?")

import sys

if "__main__" == __name__:
	if len(sys.argv) > 1:
		print("How do you know sys.argv has been used?")
		print("Did you know these are the contents of sys.argv?", sys.argv)
