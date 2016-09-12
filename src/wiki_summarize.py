import sys
import wiki_get

def usage():
    print("USAGE:")
    print("Argument\tAction")
    print("-s or --search\tGet search results for string and select from list")
    print("-f or --first\tGet first search result (I'm feeling lucky!)")
    print("no input\tGo to page if it exists, else search")
    print("-h or --help\tView this message")

def combine(strs):
    retStr = ""
    for addStr in strs:
        retStr += addStr + " "
    return retStr[:-1]

def main(argv, argc):
    
    if argc is 2 and (argv == ['-h'] or argv == ["--help"]):
        usage()
        return

    for instr in argv:
        if instr == "-s" or instr == "--search":
            print("SEARCHING")

        elif instr == "-f" or instr == "--first":
            # Get first article for result
            print("GETTING FIRST")

        elif instr.startswith("-"):
            print("Invalid argument entered.\n")
            usage()

        else:
            print("DEFAULT BEHAVIOR")
            wikiStr = combine(argv[1:])
            wiki_get.summarize(wikiStr)

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        usage()
    else:
        main(sys.argv[1:], argc)
