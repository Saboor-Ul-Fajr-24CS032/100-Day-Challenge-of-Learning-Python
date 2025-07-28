Day 67 -> Requests Module in python

requests.get(url) :
It sends a request to the given URL and gets the response (like the page’s content).

response.text :
It gives the HTML content of the web page as a string.

BeautifulSoup(html, 'html.parser') :
It parses (reads and organizes) the HTML using Python's built-in HTML parser.

soup.prettify() :
It returns the HTML in a nicely formatted, indented way.

soup.find_all("h1") :
It finds and returns all <h1> tags from the HTML.

heading.text :
It extracts only the text inside an HTML tag.
