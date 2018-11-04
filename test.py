import re
# reg = re.compile(r'/^\S+@[\w\d.-]{2,}\.[\w]{2,6}$/iU')
# is_valid = reg.match('hasinoorit@gmail.com')
# if not is_valid:
# 	print("not valid")
# else:
# 	print("valid")
if re.match('^[a-z]{3,8}$', "ha"):
	print("match")
else:
	print("Not match")