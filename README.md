# Climate Crackers 
### Team ShrimpCrackers - Puneet Johal, Tania Cao, Joyce Liao, Sophia Xia

[Live link](http://68.183.221.237:8000/)

## Project Overview
Climate Crackers is a data visualization website that allows users to explore trends in climate change in the U.S. Our landing page will be a map of the U.S. showing the percent change of the average temperatures from previous years using a color gradient. Users will be able to pick a season and year. Users will also be able to input a location (city or town name) to search for the corresponding climate data, like average temperatures and days of precipitation for each year in the past century. If the user is signed in, they will be able to save these locations onto their watchlist.

### Launch Instructions
#### Running Flask App
1. Go to [root repository](https://github.com/puneetjohal/ShrimpCrackers/) and click "Clone or Download" button
2. Copy the ssh/https link and run `$ git clone <link>`
3. Make sure the latest version of Python (currently Python 3.7.1) is installed. If not, download it [here](https://www.python.org/downloads/).
4. Install virtualenv by running `$ pip install virtualenv`
   * Make a venv by running `$ python3 -m venv ENV_DIR`
   * Activate it by running `$ . /ENV_DIR/bin/activate`
   * Deactivate it by running `$ deactivate`
5. **With your virtual environment activated**, download all of the app's dependencies by running 
```
 (venv)$ pip install -r requirements.txt
```
6. Run `$ python app.py`
7. Launch the root route (http://127.0.0.1:5000/) in your browser to go to the login page.

#### API information
##### LocationIQ
* Generate a dynamic map on the information page for each selected location
* Sign up for an account [here](https://locationiq.com/docs) to acquire an access token
##### MapQuest
* Provide coordinates of a city based on its name
* Register [here](https://developer.mapquest.com/plan_purchase/steps/business_edition/business_edition_free/register) to obtain a key; note the callback url field is optional
##### Climate Data Online
* Provides historical weather and climate data
* Request a token [here](https://www.ncdc.noaa.gov/cdo-web/token)
