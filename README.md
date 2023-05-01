# Pokeset

## About

Pokeset is a web application that allows for easy recording and querying of
custom Pokemon. Randomizers are popular game modifications wherein various
elements of a game that were previously static are made random. This app
is intended to be used for storing information from a playthrough of a
randomized Pokemon game. Where the in-game Pokedex breaks down, Pokeset
picks up the slack!

The Pokeset website has the following functionalities:

*  Create user accounts (log in)

*  User can have a Pokedex for separate games or save files

*  Record Pokemon that are found in the game. Should include:
   * Pokemon name
   * Encountered locations
   * Types (at least one, up to two)
   * Moves and abilities
   * Effectivenesses and weaknesses based on types
   * Evolution

* Search and filter Pokemon
* 
## Set-up

Follow these steps to run this repository locally:

1. Install [Python](https://www.python.org/downloads/) 
2. Install [MySQL Community Server](https://dev.mysql.com/downloads/mysql/), following the [instructions](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/) for your operating system.
3. Install [mysqlclient](https://pypi.org/project/mysqlclient/) using [pip](https://pypi.org/).
4. Install [Django](https://docs.djangoproject.com/en/4.1/intro/install/) using pip.
5. Log into MySQL and create a new database called "pokeset_db", like so:
```
mysql -u 'YOUR_USERNAME' -p
CREATE DATABASE pokeset_db;
```
6. Under the project folder "pokeset", create a file named "my.cnf" with this text with "YOUR_USERNAME" and "YOUR_PASSWORD" replaced appropiately:
```
[client]
database = pokeset_db
host = localhost
user = YOUR_USERNAME
password = YOUR_PASSWORD
default-character-set = utf8
```
7. You should now be able to run the server with ```python3 manage.py runserver```. Don't forget to migrate (```python3 manage.py migrate```).

## Testing

Various test cases for the website have been implemented using automated testing. Everytime a push is made to the main branch, Github Actions will run each test case to check that the website is working correctly.

However, if you want to run the automated testing on your computer, you will first need to install [Selenium](https://www.selenium.dev/) using pip. After Selenium is installed, enter ```python3 manage.py test``` to run the test cases on your computer. Most test cases use Google Chrome, so the automated testing may not run properly if Google Chrome is not installed on your computer. Don't forget to migrate (```python3 manage.py migrate```).

Coverage.py has also been used in testing to measure the code coverage of the website that has been tested. The coverage program runs each time changes are pushed to the Github repository and can be found in "Create Coverage Report" in the workflow report.

To generate a coverage report on your computer:

1. Install [Coverage.py](https://coverage.readthedocs.io/en/6.5.0/) using pip.
2. Run ```coverage run --source='.' manage.py test``` to collect coverage data from the automated testing.
3. Run ```coverage report``` for a report of the results.
4. Run ```coverage html``` for a HTML presentation of the report. Open htmlcov/index.html to view the report.
