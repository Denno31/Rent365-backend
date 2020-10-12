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
