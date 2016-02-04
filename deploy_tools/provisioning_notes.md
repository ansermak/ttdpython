## Required packages:
* nginx
* Python 3
* Git
* pip
* virtualenv

eq, on Ubuntu:
    sudo apt-get install nginx git python3 python3-dev
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eq, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eq, staging.my-domain.com

## Folder structure:

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv

