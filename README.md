> Crawl the takeaway platform merchant data to generate a comparable view [React based front-end](https://github.com/stefanJi/pear-web)

[中文 Readme](./README_zh.md)

# Project structure

![](http://image.youcute.cn/18-10-9/32638624.jpg)

|Module|File Directory|Description|
|:---:|:---:|:---:|
|Http service|web| API interface implementation, based on Flask|
|Crawler implementation|crawlers| crawler specific implementation|
|Crawler task execution|jobs|message scheduling based on message queue (beanstalkd)|
|Data Operations|models|CRUD operation implementation of the database, based on Sqlalchemy|

# Crawler design

![](http://image.youcute.cn/18-10-9/31686846.jpg)

# database

![](http://image.youcute.cn/18-10-9/9548846.jpg)

# Api

- [x] Login to register `/auth/login` `auth/signup`
- [x] Interface to be logged in, add validation using decorator
- [x] Login ele.me
- [x] Ele merchant crawlers
- [x] Ele merchant dish crawlers
- [x] Ele merchant comment crawlers
- [x] Ele data analysis
- [x] Meituan data crawling

- `auth/login` `auth/signup` POST
- `config_ele_crawler/sms_code` GET
- `config_ele_crawler/login_ele` GET
- `config_ele_crawler/search_address` GET
- `config_ele_crawler/get_restaurants` GET
- `crawler/task` POST
- `crawler/task` GET
- `crawler/task/<int:crawler_id>` GET
- `crawler/task/<int:crawler_id>` DELETE
