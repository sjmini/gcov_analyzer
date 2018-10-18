import sys

def main():
	flag = False
	total = 0;
	filename = sys.argv[1]
	print "filename is " + filename

	f = open(filename, 'r')
	while True:
		line = f.readline()
		if not line: break
	
		tmp = line.split(" ")
		if (tmp[0] == "function") and (tmp[3] == "2"):
			if flag == False:
				total = 0	
				print "function name: " + tmp[1]
				flag == True
			
			elif flag == True:
				print "Total number of branches: " + str(total)
				total = 0	
				print "function name: " + tmp[1]
		elif (tmp[0] == "branch"):
			total += 1	
	
	print "Total number of branches: " + str(total)
	f.close()

if __name__ == '__main__':
	main()
