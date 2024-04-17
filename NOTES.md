
# Errors and Possible solutions 

#### Can't locate revision identified by '...' when migrating using Flask-Migrate
- flask db revision --rev-id e39d16e62810  
- flask db migrate  
- flask db upgrade

#### Target database is not up to date
- flask db stamp head  # To set the revision in the database to the head, without performing any migrations. You can change head to the required change you want.
- flask db migrate  # To detect automatically all the changes.
- flask db upgrade  # To apply all the changes.

####  One or more mappers failed to initialize - can't proceed with initialization of other mappers.
- reference the table name on relationsships e.g
``` balances = db.relationship('Balance', backref='balance', lazy=True)    leaves = db.relationship('Leave', backref='leave', lazy=True) ```


#### Please edit configuration/connection/logging settings in '.../migrations/alembic.ini' before proceeding.
- just do flask db migrate

 