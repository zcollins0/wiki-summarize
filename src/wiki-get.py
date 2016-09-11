import wikipedia

def summarize(topic):
	try:
		print(wikipedia.summary(topic))
		return[]
	except (IndexError, wikipedia.PageError):
			print("Invalid page... searching")
			t = wikipedia.search(topic)
			if(t = []):
				print("No results match your search.")
			return(t)
summarize("squid")