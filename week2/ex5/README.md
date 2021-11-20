## Exercise5: Practice web scraping using beautifulsoup & requests python library

- Check out [Beautifulsoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [scrape.py](scrape.py) contains a script to retrieve a list of universities in the U.S. from [this](https://www.4icu.org/us/universities/) site.

- Create a virtual environment 
    - `python3 -m venv scraper`
- Activate virtual env
    - `source scraper/bin/activate`
- Install **beautifulsoup** and **requests** library
    - `pip3 install requests`
    - `pip3 install beautifulsoup4`
    - `pip3 install selenium`

- Run
    `python3 scrape.py`
- Result is saved to a txt [file](university_list.txt)

- For running selenium based scraper, download a driver of your browser choosing and put it inside the project folder
	- Checkout [selenium docs].(https://selenium-python.readthedocs.io/api.html)
