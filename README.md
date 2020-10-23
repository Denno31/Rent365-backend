# Rent365
A platform for users to rent items

## Prerequisites
- Have GIT, Python, PIP installed.


## Setup
1. Clone the repository
2. `cd rent365-backend`
3. `pip install -r requirements.txt`.
4. Set up local postgres DB
5. Create a .env file, add the following information
`SECRET_KEY=<secret_key>
DEBUG=TRUE
DB_NAME=<db_name>
DB_USER=<db_user>
DB_PASSWORD=<db_password>
DB_HOST=127.0.0.1
MODE=dev
ALLOWED_HOSTS=*
DISABLE_COLLECTSTATIC=1`.
6. Run database migrations.
7. Run the applocation

## API EndPoints
- https://documenter.getpostman.com/view/6565910/TVRn4nab
- https://api-rent365.herokuapp.com:- API link

1. `/shop/api/items-list`, Returns an array of items<br/> Method:- `GET`<br/> 
    Result:- `[ {
        "id": 1,
        "title": "Nike Sneakers",
        "price": 40,
        "discount_price": null,
        "category": "OW",
        "slug": "sneaker",
        "description": "Nice sneakers for that special event",
        "item_pic": "/media/uploads/bulb.jpg"}]`
2. `/shop/api/item-detail/<int:id>`, Return a single item<br/> Method:- `GET`<br/>  Result:- `{
        "id": 1,
        "title": "Nike Sneakers",
        "price": 40,
        "discount_price": null,
        "category": "OW",
        "slug": "sneaker",
        "description": "Nice sneakers for that special event",
        "item_pic": "/media/uploads/bulb.jpg"}`
3. `/accounts/api/auth/register`, Registers a user<br/>  Method:- `POST`<br/>  postData:-`{"username":"jane",
    "email":"jane@gmail.com",
    "password":"123456"}`<br/>Result:- `{
    "user": {
        "id": 2,
        "username": "jane",
        "email": "jane@gmail.com"
    },
    "token": <>
}`
4. `/accounts/api/auth/login`, Logs in a user<br/>  Method:- `POST`<br/>  postData:-`{"username":"jane",    
    "password":"123456"}`<br/>Result:- `{
    "user": {
        "id": 2,
        "username": "jane",
        "email": "jane@gmail.com"
    },
    "token": <>
}`
5. `/shop/api/item/:item_id/add_to_cart`, adds item to cart, takes item id as a param<br/> Method:- `POST` <br/> Headers:- Authorization Token --your token--.
6. `/shop/api/item/all_items`, gets all items in the cart, <br/> Method:- `GET`<br/> Headers:- Authorization Token --your token--.
7. `/shop/api/item/:item_id/remove_from_cart`, adds item to cart, takes item id as a param<br/> Method:- `POST` <br/> Headers:- Authorization Token --your token--.