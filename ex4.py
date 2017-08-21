#from sys import argv

#scrpit,filename = argv

#txt = open(filename)
print "Please input your filename:"

filename = raw_input("> ")

print "Here is your file : %s"% filename

print open(filename).read()
