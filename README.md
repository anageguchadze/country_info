# country_info

A Django REST Framework project for managing country data, including filtering, search, pagination, and caching using Redis.

## 📦 Features

- List, create, retrieve, update, and delete country entries
- Filter by fields using `django-filter`
- Search by name and ID
- Pagination (limit/offset)
- Caching for optimized list performance (Redis)
- Logging for cache hits/misses

## 📁 Project Structure

country_pro/
├── country_app/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── filters.py
├── country_pro/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/anageguchadze/country_info.git
cd country_info

2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

You can generate a requirements.txt file with:
pip freeze > requirements.txt

4. Run migrations
python manage.py migrate

5. Run Redis (if not already running)
# You need Redis installed. On Linux/macOS:

redis-server

# On Windows, use Docker or install via third party.

6. Run the server
python manage.py runserver

🔌 API Endpoints
Method	Endpoint	Description
GET	/country/	List all countries (paginated)
POST	/country/	Create a new country
GET	/country/<id>/	Retrieve a specific country
PUT	/country/<id>/	Update a country
DELETE	/country/<id>/	Delete a country

🔍 Filtering and Search
Search: /country/?search=Germany

Pagination: /country/?limit=3&offset=0

Filtering (requires you to implement in filters.py):
Example: /country/?continent=Europe&currency=Euro

🧠 Technologies Used
Python 3
Django 5.2
Django REST Framework
django-filter
Redis (for caching)

📓 Notes
Caching is implemented on the country list endpoint (CountryList) and stores paginated results.

Redis must be running locally at 127.0.0.1:6379 or configured accordingly in settings.py.