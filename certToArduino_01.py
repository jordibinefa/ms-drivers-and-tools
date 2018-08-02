#! /usr/bin/python3
# wiki.binefa.cat - 20180802
# Use:
# python3 certToArduino_01.py ca.crt arduinoCode.ino
import sys

if len(sys.argv) == 2 or len(sys.argv) == 3:
	crtFile = sys.argv[1]
	if len(sys.argv) == 3:
		inoFile = sys.argv[2]
		file = open(inoFile,"w") 
else:
	crtFile = "ca.crt"

with open(crtFile) as fin:
	for line in fin:
		line = line.replace('\n','\0')
		if "END CERTIFICATE" not in line:
			line = '"'+line+'\\n" \\'
		else:
			line = '"'+line+'\\n";'
		print(line)
		if len(sys.argv) == 3:
			file.write(line+'\n')
if len(sys.argv) == 3:
	file.close()
