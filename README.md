# bruvio biotech-dashboard

This repo aims at writing code to run a google search for 'how to data engineering' and then scrape the first 5 links in that google search and store the corresponding html.

It will also create a docker container to perform such task using a simple django app.

To create this repo a template repo has been used (see: [link text](URL "https://github.com/bruvio/pyproject_template")
, useful for defining the Python virtual enviroment and containing useful script for automation (pre-commit hooks, template dockerfiles, ...

### 1. Initial Setup

**Quick Setup** (prereq: `git, python3.8`,`docker` )

```bash
git clone <reponame>
python -m venv .env3.8
pip install -r requirements.txt
```

#### Project Structure:

Mono-repo style

```
├── AWS_deploy.sh
├── constraints.txt
├── docker-compose.yaml
├── Dockerfile
├── docker-task.sh
├── isort.cfg
├── LICENSE.md
├── orphan_branch.sh
├── project_setup.sh
├── __pycache__
│   ├── google_search_utils.cpython-38.pyc
│   └── main.cpython-38.pyc
├── pytest.dockerfile
├── pytest.ini
├── README.md
├── README_task.md
├── requirements-dev.txt
├── requirements.txt
├── saved
├── search_engine-project
│   ├── db.sqlite3
│   ├── engine
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       └── __init__.cpython-38.pyc
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── engine
│   │   │       ├── about.html
│   │   │       ├── home.html
│   │   │       └── password.html
│   │   ├── tests
│   │   │   ├── conftest.py
│   │   │   ├── __init__.py
│   │   │   └── test_search.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── manage.py
│   ├── search_engine
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── utils
│       ├── google_search_utils.py
│       └── __init__.py
└── templates
    ├── core-infrastructure-setup.yml
    └── ecs-webapp-stack.yml

```

- `search_engine-project`: contains the django webapp
- `search_engine-project/engine/tests/`: tests for basic operations on the app.
- `search_engine/utils/`: help functions
- `Dockerfile`: dockerfile for building an image and future deployment to AWS (or other cloud provider)
- `pytest-Dockerfile`: dockerfile for local testing
- `.github`: folder containing 2 workflows for automation: one tests the app in a github runner, the second builds a docker image
- `docker-task`: script to simplify operations with docker
- `AWS_deploy.sh`: script to deploy on AWS
- `templates/`: folder containing cloudformation scripts to deploy on AWS

### 4. Starting the environment

# option a

To start the app locally from the terminal run

`./run.sh`

The service will start listening at

`http://127.0.0.1:8000`

# option b

To start the app from a docker container from the terminal run

`./docker/task.sh buildrun`

The service will start listening at
`http://localhost:9999`

### 5. Building Docker image

To create a docker image (withou using my docker-task script)run

```
docker build -t python-django-app-search .
```

### 6. Running app from container locally

To run the app from the container locally run from the terminal

```
docker run -i -p 8000:8000 -d python-django-app-search
```

and then from the browser visit

```
localhost:8000
```

### 7. local testing using a docker container

To run a local test using a docker container run

```
docker-compose up
```

### 8. deploy to AWS

to deploy to AWS, I included two bash script to simplify operation

A prerequisite is to have setup AWS cli and a profile.

Run first

`..`

this will display how to use the script

First create a new repository on ECR

`./docker-task.sh createrepo`

then build and push the docker image to ECR

`./docker-task.sh buildpush`

This will push into your ECR repository called biotech (edit the docker-task.sh file to change defaults name)

now just run

`./AWS_deploy.sh`

this will start the creation of two Cloudformation stacks: 1) for the core infrastructure (VPC, SG, subnets..) the other will start a ECS cluster.

After 5/10 minutes you will find on the terminal the DNS of the application load balancer.
Copy and paste it into a browser tab to launch the app.

## Authors

- **Bruno Viola** - _Initial work_ - [bruvio](https://github.com/bruvio)
