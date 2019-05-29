# Climate Crackers 
### Team ShrimpCrackers - Puneet Johal, Tania Cao, Joyce Liao, Sophia Xia

[Live link](http://68.183.221.237:8000/)

## Project Overview
Climate Crackers is a data visualization website that allows users to explore trends in climate change in the U.S. Our landing page will be a map of the U.S. showing the percent change of the average temperatures from previous years using a color gradient. Users will be able to pick a season and year. Users will also be able to input a location (city or town name) to search for the corresponding climate data, like average temperatures and days of precipitation for each year in the past century. If the user is signed in, they will be able to save these locations onto their watchlist.

### Launch Instructions
#### Install and run on localhost
1. Go to [root repository](https://github.com/puneetjohal/ShrimpCrackers/) and click "Clone or Download" button
2. Copy the ssh/https link and run `$ git clone <link>`
3. Make sure the latest version of Python (currently Python 3.7.1) is installed. If not, download it [here](https://www.python.org/downloads/).
4. Install virtualenv by running `$ pip install virtualenv`
   * Make a venv by running `$ python3 -m venv ENV_DIR`
   * Activate it by running `$ . /ENV_DIR/bin/activate`
   * Deactivate it by running `$ deactivate`
5. Move to the climate_crackers directory: `$ cd climate_crackers/`
6. **With your virtual environment activated**, download all of the app's dependencies by running 
```
 (venv)$ pip install -r requirements.txt
```
7. Run `$ python __init__.py`
8. Launch the root route (http://127.0.0.1:5000/) in your browser to go to the login page.

#### Install and run on Apache2
1. SSH into your droplet by running `$ ssh <user>@<droplet_ip_address>`. Your user account should be part of the sudo group on the droplet.
2. Move to the www directory using `$ cd ../../var/www/`
3. Clone the repo by running `$ sudo git clone https://github.com/puneetjohal/ShrimpCrackers.git`
4. Move into the repo directory using `$ cd climate_crackers/`. Use `$ sudo vim climate_crackers.conf` to edit the conf file. Change the parameter after "ServerName" to the IP address of your droplet. Save and exit, and move the conf file to the sites-enabled directory by running `sudo mv climate_crackers.conf /../../etc/apache2/sites-enabled/`
5. Enable the site by running `$ sudo a2ensite climate_crackers`
6. Make sure the latest version of Python (currently Python 3.7.1) is installed on your droplet by running `$ python3.7 --version`. The terminal should output `Python 3.7.1`. If not, run
```
  $ sudo apt-get update
  $ sudo apt-get install python3.7
  $ python3.7 --version
```
7. Install virtualenv by running `$ pip install virtualenv`
   * Make a venv by running `$ python3 -m venv ENV_DIR`
   * Activate it by running `$ . /ENV_DIR/bin/activate`
   * Deactivate it by running `$ deactivate`
8. **With your virtual environment activated**, download all of the app's dependencies by running 
```
 (venv)$ pip install -r requirements.txt
```
9. Run `$ sudo service apache2 restart` to restart the Apache server.
10. The app is now being hosted on port 8000 of your droplet. Go to http://<droplet_ip_address>:8000/ in your browser to view the site.

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
