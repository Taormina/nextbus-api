import web, urllib2, json, os
from flask import Flask
from bs4 import BeautifulSoup
        
urls = ('/(.*)/(.*)/(.*)', 'hello')
app = web.application(urls, globals())

class hello:        
	def GET(self, route, direction, stop):
		f = urllib2.urlopen("http://www.nextbus.com/predictor/fancyBookmarkablePredictionLayer.shtml?a=georgia-tech&r="+route+"&d="+direction+"&s="+stop);
		soup = BeautifulSoup(f.read())
		f.close()

		prev = 0
		outArray = []

		if "Arriving" in soup.text:
			outArray.append("Arr.")
		elif "Departing" in soup.text:
			outArray.append("Dep.")
		for s in soup.find_all("div",class_="right"):
			curr = int(s.string)
			if curr < prev:
				break
			else:
				outArray.append(curr)
				prev = curr

		return json.dumps({"predictions": outArray if outArray else "errors"})

if __name__ == "__main__":
	app.run()
