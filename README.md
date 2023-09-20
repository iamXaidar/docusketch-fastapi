# DocuSketch Fast Api Test Project

To run this app in local machine you need pre-installed poetry and docker.
## Clone repository from GitHub
- ```$ git clone ```
- ```$ cd DocuSketchTest_FastApi ```
## Install dependencies
- ```$ poetry install```
## Create dotenv file with db and web credentials by example in .env.template
- ```$ make create_dotenv```
## Up Postgresql database container
- ```$ make up```
## Make migrations
- ```$ make init_db```
## Import data to Postgresql server
- ```$ make import```
## Start application
- ```$ make startapp```