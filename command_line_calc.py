import sys
args = [i for i in sys.argv]
try:
  op = args[1]
except IndexError:
	print("Please specify the operation")
	exit()
if op == "add":
	print(f"Sum: {sum([float(i) for i in args[2:]])}")
elif op == "sub":
	start = float(args[2])
	for i in args[3:]:
		start -= float(i)
	print(f"First - all: {start}")
else:
	print(f"{op} is not a valid operation.\nValid operations are: add, sub") 
	
