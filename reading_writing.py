# Reading and writing of text files
# with: context manager. It closes automatically the stream when finished
# modes: r: reading, w: write, a: append text
# to work with images, we have to open the file in binary mode (just add a b, rb and wb)

def copy():
	# Copy the content of example.txt to a new file called "copy.txt"
	with open('example.txt', 'r') as rf:
		with open('copy.txt', 'w') as wf:
			for line in rf:
				wf.write(line)
			wf.write("\ncopy succesfully")

def read():
	with open('example.txt', 'r') as f:
		# for line in f:
		# 	print(line, end="")

		# We'll read 20 characters each time
		size = 20
		content = f.read(size)

		# content contains 20 characters
		# when it runs out of characters, it returns an empty string

		while len(content) > 0:
			print(content, end="")
			content = f.read(size)

# copy()