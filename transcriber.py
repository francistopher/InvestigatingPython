# written while listening to Dr. Andrew Steindog in Discrete

import sys

class Transcriber:
	
	def __init__(self):
		fileNames = self.__getFileNames()

		self.inputFileName = fileNames[0]
		self.outputFileName = fileNames[1]
		self.commentaryFileName = fileNames[2]
		self.outputFileContents = self.__readInputFile()
		self.__buildOutputFile()
	
	def __getFileNames(self):
		if len(sys.argv) > 3:
			return (sys.argv[1], sys.argv[2], sys.argv[3])
		elif len(sys.argv) > 2:
			return (sys.argv[1], sys.argv[2], "commentary.txt")
		elif len(sys.argv) > 1:
			return (sys.argv[1], "output.py", "commentary.txt")
		else:
			return ("input.py", "output.py", "commentary.txt")
	
	def __readInputFile(self):
		try:
			commentaryContents = ""
			inputContents  = ""
			with open(self.commentaryFileName, "r") as commentaryFile:
				 commentaryContents = commentaryFile.read()
			with open(self.inputFileName, "r") as inputFile:
				 inputContents = inputFile.read()
		except FileNotFoundError:
			print("Input File Doesn't Exist")
			sys.exit()
		return self.__toPrintStatement(commentaryContents + self.__getHeaderFooter() + inputContents + self.__getHeaderFooter(False))

	def __getHeaderFooter(self, isHeader=True):
		if isHeader:
			fileNameLen = len(self.outputFileName)
			dashesLen = (98 - fileNameLen) // 2
			return '\n' + (dashesLen * '-') + self.outputFileName + (dashesLen * '-') + '\n' 
		else:
			return '\n' + (100 * '-') + '\n'
	
	def __toPrintStatement(self, contents):
		return 'print("""' + contents + '""")'
	
	def __buildOutputFile(self):
		outputFile = open(self.outputFileName, "w")
		outputFile.write(self.outputFileContents)
		print("Output file built")

if "__main__" == __name__:
	t = Transcriber()
	
