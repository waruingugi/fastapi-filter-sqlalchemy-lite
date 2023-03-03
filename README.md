# FastAPI filter

## Compatibility

**Required:**
  * Python: >=3.8, <3.12
  * Fastapi: >=0.78, <0.93
  * Pydantic: >=1.10.0, <2.0.0


**Optional**
  * SQLAlchemy: >=1.4.36, <2.1.0

## Installation
---

```bash
# Lite version
pip install fastapi-sqlalchemy-filter-lite
```

## Documentation
---
This package was inspired by [arthurio](https://github.com/arthurio/fastapi-filter)  

The package is a lite version for **SQLAlchemy only** with a few modifications to it.

Please visit this site to view the full documentation: [https://fastapi-filter.netlify.app/](https://fastapi-filter.netlify.app/)

## Modifications / Additions
---
### You can import the `Filter` class and create a filter on the fly:
```bash
from fastapi_sqlalchemy_filter import Filter

user_dict = {'name': 'Jon Snow', 'clan': 'Targaryen'}
user_filter = Filter(**user_dict)
```

### Package returns `None` if an ordering field is not present on the class definition.
### *Note: No user action is needed on this part*
This function was modified from:
```bash
...
    @property
    def ordering_values(self):
        """Check that the ordering field is present on the class definition."""
        try:
            return getattr(self, self.Constants.ordering_field_name)
        except AttributeError:
            raise AttributeError(
                f"Ordering field {self.Constants.ordering_field_name} is not defined. "
                "Make sure to add it to your filter class."
            )
...
```

To
```bash
...
    @property
    def ordering_values(self):
        """Check that the ordering field is present on the class definition."""
        if hasattr(self, self.Constants.ordering_field_name):
            return getattr(self, self.Constants.ordering_field_name)
        return None
...
```