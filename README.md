## Autocomplete feature using trie data structure


**Autocomplete**, or **word completion**, is a feature in which an application predicts the rest of a word a user is typing. 

Here I have implemented an API for this feature using **Trie** data structure.  API server is implemented using [flask](https://flask.palletsprojects.com/en/1.0.x/). The source code is written in python.

The database used here is a csv file which contains names of people. The app loads all the data in memory whenever the server is started and insert all the names into trie. When the autocomplete API is triggered, then a prefix search operation is done on the existing trie. 

### Requirements
 - Ubuntu
 - python 2.x (or higher)
 - pip (pip3 in case of python3)
 - flask
### Install
- Python
 ```
	sudo apt-get install python
```
- Pip
```
	sudo apt-get install python-pip
```
- Flask
```
	pip install flask
```
### Usage

- Go to the app folder and run following command:
```
	python app.py
```
- Open any browser and go to `127.0.0.1/home` . You should see an html page with a search bar.
- Type at-least 3 letters to get results.

### References
- [Autocomplete feature](https://en.wikipedia.org/wiki/Autocomplete)
- [Trie](https://en.wikipedia.org/wiki/Trie)
- [Auto-complete feature using trie](https://www.geeksforgeeks.org/auto-complete-feature-using-trie/)

![](https://github.com/abhijais04/Search-bar-Autocomplete/blob/master/AutoComplete.png)

