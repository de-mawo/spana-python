# Spana Python Flask Version





python3 -m venv .venv


. .venv/bin/activate

python -m pip freeze > requirements.txt

pip uninstall -r requirements.txt -y

pip install -r requirements.txt

printenv



docker exec -it container_name_or_id bash



psql postgres://user:password@ip_add_or_domain:port/db_name




flask db init
flask db migrate
flask db upgrade

#### To Run the Server in Terminal
flask run

#### To Run the Server with specific host and port
# flask run -h HOSTNAME -p PORTNUMBER
flask run -h 127.0.0.2 -p 5001

#### To Run the Server with Automatic Restart When Changes Occur
FLASK_DEBUG=1 flask run


