# Overview

**This is demo project.**

It's a library API, which is contains 100 000 books and 50 000 readers. Each reader has n-books related with them. API provide acccess to the details of each reader by `ID` and all books related to them and allows to extract all of data into `CSV`.

## Database

I use two `PostgreSQL 12.1` servers, for implementation of master-slave replication mode. The master instance handles read/write operations and slave run in a `hot_standby=on` mode and allow only to read operations. On the app layer, I've changed the default behavior of database access, for read operations app will use slave server, for writing master.

**N.B.**: This solution doesn't appropriate for production. It has many limitations, but for the demo, I guess, enough.

## App

I've changed the default Django project template, all Django apps and related code I have moved into the `apps` folder, but `api` keep in a root. App config code stored in the `conf` folder. The `core` folder contains base model classes, mixins and some utils for CSV data preparations. This is not finished the structure of code organization, for example, I may move code from utils into a module that will be resposible for the business logic of the app.

## Api

Endpoints:
`api/v1/readers/<int:id>` - Reader endpoint
`api/v1/export` - for downloading all data.

## How to run

Just run in a console `docker-compose -f stack.yml up`
Initial run will take awhile for populating database with fake data. If you need populate fake data again, please make sure that `migrations` folder doesn't contain file `0001_initial.py`.
