from distutils.core import setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name = "fastapi_sqlalchemy_filter",
    packages = ['fastapi_sqlalchemy_filter'],
    version = "0.2.4",
    author = "Warui",
    author_email = "waruingugientp@gmail.com",
    description = "A lite version of fastapi-filter for SQLAlchemy only",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/waruingugi/fastapi-filter-sqlalchemy-lite/tree/sqlalchemy-filter-lite",
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
    download_url = "https://github.com/waruingugi/fastapi-filter-sqlalchemy-lite/archive/refs/tags/v0.2.4.tar.gz",
    keywords = ['FastAPI', 'SQLAlchemy', 'Filter'],
    install_requires=[
        'pydantic',
        'fastapi',
        'sqlalchemy',
    ],
)
