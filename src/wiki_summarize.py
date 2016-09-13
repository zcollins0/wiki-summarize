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
    retStr = " ".join(strs)
    return retStr

def main(argv):
    print("")
    if argv[0] == "-h" or argv[0] == "--help":
        usage()

    elif argv[0] == "-s" or argv[0] == "--search":
        print("SEARCHING")

    elif argv[0] == "-f" or argv[0] == "--first":
        # Get first article for result
        print("GETTING FIRST")

    elif argv[0].startswith("-"):
        print("Invalid argument entered.\n")
        usage()

    else:
        wikiStr = combine(argv[:])
        wiki_get.summarize(wikiStr)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        main(sys.argv[1:])
