import wikipedia
from bs4 import BeautifulSoup
w = ""
soup = BeautifulSoup(w, "html.parser")

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



