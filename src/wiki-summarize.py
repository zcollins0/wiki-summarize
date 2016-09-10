import sys
#import wiki-get

def usage():
	print("USAGE STUFF\n")

def main(argv):
	argc = len(sys.argv)
	if argc is 1 and argv is "-h":
		usage()

if __name__ == "__main__":
	main(sys.argv[1:])
