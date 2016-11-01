import wikipedia

# function to call to summarize. if summarizing doesn't work then search.
def summarize(topic):
	try:
		print(wikipedia.summary(topic))
		return []
	#catch exceptions so users don't see block of error messages	
	except (IndexError, wikipedia.PageError, wikipedia.DisambiguationError):
			print("Invalid page. Searching...")
			t = wikipedia.search(topic)
			if(t == []):
				print("No results match your search.")
			return(t)

# function to call to search
def search(topic):
	t = wikipedia.search(topic)
	if(t == []):
		print("No results match your search.")
	else:
		print(t)
	return(t)
	
# function to call to get summary, or first search result if that doesn't work
def imFeelingLucky(topic):
	try:
		print(wikipedia.summary(topic))
	except (IndexError, wikipedia.PageError, wikipedia.DisambiguationError):
		t = wikipedia.search(topic)
		if(t == []):
			print("No results match your search.")
		else:
			p = wikipedia.page(t[1])
			print(p.title + ":")
			print(wikipedia.summary(t[1]))

