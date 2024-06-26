# Restaurant Search Project

This Django project allows users to search for restaurants and their dishes using a search form. The project includes functionalities for loading restaurant data from a CSV file and displaying search results.

## Features

- Load restaurant data from a CSV file
- Search for restaurants and their dishes
- Display search results with matching dishes

## Prerequisites

- Python 3.x
- Django 3.2.x

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/restaurant_search_project.git
cd restaurant_search_project
```
### 2. Run below commands
```
pip install -r requirements.txt
python manage.py migrate
python manage.py load_restaurants --path=path/to/your/file.csv
python manage.py runserver
```

