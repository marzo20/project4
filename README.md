# Project4
## Niche Market

### Installation

- Fork and clone
- cd to the cloned directory
- pip3 install django, pillow, and smartcar
- python3 mangae.py runserver

### Technologies

- Python
- Django
- pillow
- CIS VIN DECODER API
    https://cis-vin-decoder.p.rapidapi.com/vinDecode
- crispy form
- django money

### Description

- Online community that shares used car price and leased car price. 

### MVP Goal
- Login Authentication working
- User can create, edit, delete posts
- User is able to upload image for posts
- Request json data using api and render in template.
- User can search data using vin#
- Styling using css

### Stretch Goals
- User can search fair price range of a car using API
- User can search a car information and specs using API
- 
### Wireframes
![ERD](/pitch/erd.png)
![Wireframe](/pitch/wireframe.png)

### User stories

- User wants to sign in community
- User wants to login community
- User wants to share information about cars and lease.
- User wants to post their own car if they wants to sell their leased car
- User wants to see other users' posts if there is a car they are looking for with good condition and reasonable price.

### Restful Routing Chart

| VERB | URL pattern | Action \(CRUD\) | Description |
| :--- | :--- | :--- | :--- |
| GET | /users/login|\(Read\) | Show loginPage |
| POST | /users/login|\(Read\) | Check authentication and authorize |
| GET | /users/register |\(READ\) | Show Sign Up Page |
| POST | /users/register |\(Create\) | Create User/authentication and authorization |
| POST | /users/edit |\(Update\) | Route to Update profile Info in DB |
| POST | /users/changepassword |\(Update\) | Route to Update Password in DB |
| GET | /users/logout |\(Read\) | logout |
| GET | /users/profile |\(Read\) | Shows users profile Page |
| POST | /users/profile |\(UPDATE\) | Update user's profile |
| POST | /users/changepassword |\(UPDATE\) | Change user's password |
| GET | /community/posts |\(Read\) | Show all of user's posts|
| POST | /community/postform |\(Create\) | Create a post about a dish |
| GET | /community/posts/:id |\(READ\) | Show details about a dish post|
| POST | /community/post/:id/edit |\(UPDATE\) | Edit selected post|
| DELETE | /post/:id |\(DELETE\) | Delete the post |
| GET | /search |\(Read\) | show search results |
| GET | /car/:vin# |\(Read\) | Show information of a car|