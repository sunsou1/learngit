from sys import argv

script,user_name = argv
prompt = "> "

print "hi %s,I'm the %s script. "%(user_name,script)
print "Do you like me %s? "% user_name
likes = raw_input(prompt)