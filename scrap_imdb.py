def get_page(page):

        import urllib2
	
	try:
		source = urllib2.urlopen(page)
		val = source.read()
		source.close()
		return val
	except:
		return ""


def tcast(movie):
        
        tstart = movie.find("<meta property='og:title")
        tstart_quote = movie.find('"', tstart)
        tend_quote = movie.find('"', tstart_quote+1)
        print "Name: " + movie[tstart_quote+1:tend_quote]
	
	print "Cast: "

        cast1 = movie.find('Stars:')
	cast2 = movie.find('See full cast and crew')
	cast = movie[cast1:cast2]
	
	
	while True:
		
		cstart1 = cast.find('"name"')
		if cstart1 == -1:
		        break
		cstart = cast.find('>', cstart1)
		cend = cast.find('</span>', cstart)
		print cast[cstart+1:cend]
		cast = cast[cend:]
        

def get_next_target(s):
        	
	start_link = s.find('<a href=')
	
	if start_link == -1:
		return None, 0
	
	start_quote = s.find('"', start_link)
	end_quote = s.find('"', start_quote + 1)
	url = s[start_quote+1:end_quote]
	return url, end_quote	


def get_all_links(text):

	url_list = []
	while True:
		url, end_quote = get_next_target(text)
	
		if url:
			text = text[end_quote:]
			url_list.append(url)
		else:
			break
	
	
	for i in range(0, num):
		var = get_page('http://www.imdb.com' + url_list[i])
		tcast(var)
		

seed = "http://www.imdb.com"
num = int(raw_input("How many box- office movies need to be shown? (max 5): "))
page = get_page(seed)

start_text = page.find('Now Playing (Box Office)')
end_text = page.find('<a href="/chart/?ref_=hm_cht_sm">')
lookup = page[start_text:end_text]

get_all_links(lookup)

raw_input()