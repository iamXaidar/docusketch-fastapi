# DocuSketch Fast Api Test Project

To run this app on local machine you need pre-installed poetry and docker.

```
api: package contains endpoints

config: project configuration directory, that contains settings module

data: other data that used in development

db: db configuration package

logs: project logging configuration directory that contains app.log file

migrations: alembic migrations configuration

test: pytest
```
**Note:**
```
I used docker to build db server, I thought it is simpler than install and configure Postgres on local machine...
But I did not implement main web app by docker, because I supposed it is just test project and there is no reason to...
```

## Clone repository from GitHub
- ```$ git clone https://github.com/iamkhaidarzakirov/DocuSketchTest_FastApi.git```
- ```$ cd DocuSketchTest_FastApi ```
## Install dependencies
- ```$ poetry install```
## Create dotenv file with db and web credentials by example in .env.template
- ```$ make create_dotenv```

- **Note:** All docker db container credentials are specified in template because it is not a real project... 
## Up Postgresql database container
- ```$ make up```
## Make migrations
- ```$ make init_db```
- **Note**: If error raises (...port 5433 failed: server closed...), you need repeat the above command
## Import data to Postgresql server
- ```$ make import```
## Start application
- ```$ make startapp```
