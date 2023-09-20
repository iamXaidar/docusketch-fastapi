# DocuSketch Fast Api Test Project

To run this app in local machine you need pre-installed poetry and docker.
## Clone repository from GitHub
- ```$ git clone https://github.com/iamkhaidarzakirov/DocuSketchTest_FastApi.git```
- ```$ cd DocuSketchTest_FastApi ```
## Install dependencies
- ```$ poetry install```
## Create dotenv file with db and web credentials by example in .env.template
- ```$ make create_dotenv```

P.S All docker db container credential are specified in template cause it is not a real project... 
## Up Postgresql database container
- ```$ make up```
## Make migrations
- ```$ make init_db```
## Import data to Postgresql server
- ```$ make import```
## Start application
- ```$ make startapp```
