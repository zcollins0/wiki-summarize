import sys
#import wiki-get

def usage():
	print("USAGE STUFF\n")

def main(argv):
	argc = len(sys.argv)
	print(argc)
	print(argv[0])

	if argc is 2 and argv == ['-h']:
		usage()

if __name__ == "__main__":
	print("GOING TO MAIN")
	main(sys.argv[1:])
