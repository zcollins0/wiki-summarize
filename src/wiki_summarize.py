iport sys
import wiki_get

def usage():
    print("USAGE:")
    print("Argument\tAction")
    print("-s or --search\tGet search results for string and select from list")
    print("-f or --first\tGet first search result (I'm feeling lucky!)")
    print("no argument\tGo to page if it exists, else search")
    print("-h or --help\tView this message")

# combine a set of strings, space separated
def combine(strs):
    retStr = " ".join(strs)
    return retStr

# do a search explicitly
def do_search(strs):
    arr = []
    print("Search returned:")
    for s in strs:
        print(s)

    instr = input("Input desired article: ")
    print("")
    wiki_get.imFeelingLucky(instr)

def main(argv):
    print("")
    if argv[0] == "-h" or argv[0] == "--help":
        usage()

    elif argv[0] == "-s" or argv[0] == "--search":
        # combine rest of arguments to form search string
        wikiStr = combine(argv[:])
        returned = wiki_get.search(wikiStr)
        # if we get any search results, let user select which article they want to use
        if returned != []:
            do_search(returned)

    elif argv[0] == "-f" or argv[0] == "--first":
        # Get first article for result
        wikiStr = combine(argv[:])
        wiki_get.imFeelingLucky(wikiStr)

    elif argv[0].startswith("-"):
        # unrecognized argument, print usage
        print("Invalid argument entered.\n")
        usage()

    else:
        # default behavior - summarize, and if it doesn't work, do search behavior
        wikiStr = combine(argv[:])
        returned = wiki_get.summarize(wikiStr)
        if returned != []:
            do_search(returned)

if __name__ == "__main__":
    # no input -> print usage
    if len(sys.argv) == 1:
        usage()
    else:
        main(sys.argv[1:])
