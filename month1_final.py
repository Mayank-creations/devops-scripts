import os

files = os.listdir('.')
print("Phython is reaching your files:")
for  f in files:
	print(f"-{f}")
