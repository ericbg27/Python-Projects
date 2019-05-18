#one.py
print('hello')

def func():
	print("FUNC() IN ONE.PY")

# def function():
#	pass

# def function2():
#	pass

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
	# RUN THE SCRIPT!

	# Apply some logic if it's not being imported
	# call functions
	# function()
	# function2()
	print("ONE.PY is being run directly!")
else:
	print("ONE.PY has been imported!")