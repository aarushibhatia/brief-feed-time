# Feed API time.com

### This is an API for getting top six feeds of `The Brief` section from [time.com](https://time.com/) website.

* #### Runs on Flask server having `python3` as dependency.
* #### `feeds.py` provides the list of objects for top six feeds.
* #### `BeautifulSoup` is used for the website scraping for *The Brief* section. Alternatively it can be achieved from `RSS feed`.
* #### `server.py` is the main server logic file. At `/getTimeNews` endpoint call it responses with the JSON of all the feeds
#### recieved from feeds.py.
* #### Server runs at `8000` port on localhost. (For development environment)
* #### `requirements.txt` contains all the dependencies of the project to install.

### **To run server**
* #### `Python3` and `pip` must be installed.
* #### Run `pip install -r requirements.txt` to install all the project dependencies.
* #### Run `python3 server.py` to start server at localhost.

### **API Details**
* #### You will get response from server at `http://localhost:8000/`
* #### To check is server response as needed goto `/ok`. If it get `"ok":True` then server is ready to respond.
* #### `/getTimeNews` will respond JSON with top six news feeds.

### **Response Screenshots**

![alt text](https://github.com/aarushibhatia/brief-feed-time/blob/master/screenshots/json.PNG "JSON response capture")

![alt text](https://github.com/aarushibhatia/brief-feed-time/blob/master/screenshots/time.PNG "time.com feed response capture")
