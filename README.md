# Personal Gallery


A virtual gallery of images that interest me, using django

## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes, **clone** this repository into a **virtual environment** and install the package manager, **pip**.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Use the package manager pip to install all project requirements. 
```sh
(virtual) $ pip install -r requirements.txt
```

### Installing

To get a development env running, use the **.env.example** file to create a **.env** file with appropriate values

## Running the tests

Run automated tests for this system

```sh
(virtual) $ python3 manage.py test picha
```

## Deployment

With all environment variables changed to suit your local copy of this repository, deploy the application to [Heroku](https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43) to see it live or simply run it locally
 ```
 (virtual) $ python3 manage.py runserver
 ```

## Built With

* [Django 3.0.8](https://www.djangoproject.com/) - The web framework used
* [Heroku](https://www.heroku.com/platform) -  Deployment platform
* [Python3.6](https://www.python.org/) - Backend logic
* [Postresql](https://www.postgresql.org/) - Database system


## Authors

* [Karen Ngala](https://github.com/KarenNgala)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/KarenNgala/Gallery/blob/master/LICENCE) file for details
