from distutils.core import setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name = "fastapi-sqlalchemy-filter",
    version = "0.0.1",
    author = "Warui",
    author_email = "waruingugientp@gmail.com",
    description = "A simple FastAPI filter for SQLAlchemy",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/waruingugi/fastapi-filter-sqlalchemy-lite",
    project_urls = {
        "Bug Tracker": "https://github.com/waruingugi/fastapi-filter-sqlalchemy-lite/issues",
    },
    classifiers = [
        "Natural Language :: English",
        "Framework :: FastAPI",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords = ['FastAPI', 'SQLAlchemy', 'Filter'],   # Keywords that define your package best
    install_requires=[
        'pydantic',
    ],
)
