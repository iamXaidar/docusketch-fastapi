# DocuSketch Fast Api Test Project

To run this app in local machine you need pre-installed poetry and docker.
## Clone repository from GitHub
- ```$ git clone ``` 
## Install dependencies
- ```$ poetry install```
## Create dotenv file with db and web credentials by example in .env.template
- ```$ > config/.env```
## Up Postgresql database container
- ```$ make up```
## Start application
- ```$ cd source```
- ```$ poetry run uvicorn main:app --reload```