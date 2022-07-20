# Project4
## Niche Market

### Installation

- Fork and clone
- cd to the cloned directory
- pip3 install django, pillow, and requests
- source .env/vin/activate
- python3 mangae.py runserver


### Technologies

- Python
- Django
- pillow
- CIS VIN DECODER API
    https://cis-vin-decoder.p.rapidapi.com/vinDecode
- crispy form
- django money
- requests
### Description

- Online community that lists leased vehicle for sale. 

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

![Wireframe](/pitch/wireframe.png)

### ERD

![ERD](/pitch/erd.png)
### User stories

- User wants to sign in community
- User wants to login community
- User wants to share information about cars and lease.
- User wants to post their own car if they wants to sell their leased car
- User wants to see other users' posts if there is a car they are looking for with good condition and reasonable price.

### Restful Routing Chart

| VERB | URL pattern | Action \(CRUD\) | Description |
| :--- | :--- | :--- | :--- |
| GET | /login|\(Read\) | Show loginPage |
| GET | /logout |\(Read\) | logout |
| POST | /register |\(Create\) | Create User/authentication and authorization |
| GET | /profile |\(Read\) | Shows users profile Page |
| GET | /posts |\(Read\) | Show all of user's posts|
| POST | /posts/add |\(Create\) | Create a post about a vehicle |
| GET | /posts/:id |\(READ\) | Show details about a vehicle post|
| POST | /post/:id/edit |\(UPDATE\) | Edit selected post|
| DELETE | /post/:id/delete |\(DELETE\) | Delete the post |
| GET | /info |\(CREATE\) | Show spec check page |
| GET | /info/details|\(Read\) | GET detail info from API |
| GET | /profile/add |\(READ\) | Show what user adds |
| POST | /profile/add/create |\(CREATE\) | User create vehicle in profile|
| DELETE | /profile/:pk/delete |\(DELETE\) | DELETE vehicle from profile |
|\