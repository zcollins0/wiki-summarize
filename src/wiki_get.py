import wikipedia

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
			
def search(topic):
	t = wikipedia.search(topic)
	if(t == []):
		print("No results match your search.")
	else:
		print(t)
	return(t)


