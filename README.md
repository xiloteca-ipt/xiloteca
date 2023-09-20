#### Main brach deployment: https://main-bvxea6i-d7txlva5veuyo.ca-1.platformsh.site/

#
# How to execute:

1. Create Python virtual envioronment with `python3 -m venv venv` then activate it `source venv/bin/activate`

1. Install dependencies `pip install -r requirements.txt`

2. Check Django version
`django-admin --version`

3. Execute the project
`python3 xiloteca/manage.py runserver`


# How to test:

1. Run the following command:
`python3 xiloteca/manage.py test`

You can add more details to the execution log by adding the parameter `--verbosity=VERBOSITY_LEVEL`.
Verbosity levels are: 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output.


# Infrastructure details:

The website is hosted in an Platform.sh deployment site. The database is a GCP MySql database, hosted in Google Cloud Platform.


# Contribution guide:
You can find tasks for this project in the following board: https://trello.com/b/aTcjwDVh/kanban

You should fork the project, make changes and then open a pull request to our team. New code must be covered with unit tests.

# Pipeline execution:
Commits to the `main` branch trigger a new deployment to production.

You can check pipelines execution in the following link: https://github.com/xiloteca-ipt/xiloteca/actions/workflows/django.yml (access required)