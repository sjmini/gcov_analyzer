import sys
import re

def main():
	flag = False
	branch_total = 0.0
	st_total = 0.0
	st_cover = 0.0
	filename = sys.argv[1]
	
        regex_compile_total = 0.0
        regex_compile_cover = 0.0
        regex_compile_flag = False

        print "filename is " + filename

	f = open(filename, 'r')
	while True:
		line = f.readline()
		if not line: break
	
		tmp = line.split(" ")
		#if (tmp[0] == "function") and (tmp[3] == "2"):
		if (tmp[0] == "function"):
                        #print "in function:"
                        if flag == False:
				branch_total = 0
                                if (tmp[1] == "regex_compile"):
                                    regex_compile_flag = True
				    print "function name: " + tmp[1]
                                else: 
                                    regex_compile_flag = False
				    #print "function name: " + tmp[1]
				
                                #print "function name: " + tmp[1]
				flag == True
			
			elif flag == True:
				#print "Total number of branches: " + str(branch_total)
                                if (tmp[1] == "regex_compile"):
                                    regex_compile_flag = True
				    print "function name: " + tmp[1]
                                else:
                                    regex_compile_flag = False
                                branch_total = 0
				#print "function name: " + tmp[1]
		elif (tmp[0] == "branch"):
                       # print "in branch"
                        if regex_compile_flag == True:
                            regex_compile_total += 1
                            if (line.find(' 0%') != -1):
                                print "<regex_compile function: " + line + "not executed 0%>"
                            elif line.find('never executed') != -1:
                                print "<regex_compile function: " + line + "not executed never>"
                            else:
                                regex_compile_cover += 1
                                print "<regex_compile function: " + line + "executed>"
                            #print "HSJ : " + tmp[3]
		        branch_total += 1
		elif (tmp[4] == "#####:"):
                        st_total += 1
                        #print "####" + tmp[4]
                elif (len(tmp) > 8) and re.match('[0-9+:]', tmp[8]):
              # elif re.search('[0-9]:', line):
                        st_cover += 1
                        st_total += 1
                        #print "statement : " + tmp[8]
	
	print "Total number of branches: " + str(branch_total)
	print "Total number of statements: " + str(st_total)
        #print "Statement Coverage: " + str(st_cover) + "/" + str(st_total) + " = %.2f%%" % (st_cover/st_total * 100.0)
        print "regex_compile func branch coverage: " + str(regex_compile_cover) + "/" + str(regex_compile_total) + " = %.2f%%" % (regex_compile_cover/regex_compile_total * 100.0)
	f.close()

if __name__ == '__main__':
	main()
