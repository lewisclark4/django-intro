## Git Commands for testing

Test all test files `python3 manage.py test`                                                   
Test a specific test file `python3 manage.py test todo.test_views`                                    
Test a class in a specific file `python3 manage.py test todo.test_models.TestModels`                       
Test a function in a class in a file `python3 manage.py test todo.test_models.TestModels.test_done_defaults_to_false`


## Coverage

`pip3 install coverage`
`coverage run --source=<folder name> manage.py test`
`coverage report`
`coverage html`
`python3 -m http.server`
View the coverage report in the web browser and view missing coverage.


## Postgres for Heroku

Resources
In the addons, Select **Heroku Postgres**
Click *provision*
This will create a config variable 'DATABASE_URL'

Also able to use MySQL with addon called Clear DB.

Can see on the CLI with heroku addons.


## Requirements

`pip3 install django`
`pip3 install coverage`
`pip3 install gunicorn`
`pip3 install psycopg2 binary`
`pip3 install dj_database_url` (parse the postgres config var)

## Database congif

`heroku config`