from sqlalchemy.orm import declarative_base

Base = declarative_base()

# This Base class is used to define the declarative base for SQLAlchemy models.
# It allows us to create ORM models that can be mapped to database tables.
# By using this base, we can define our models in a more Pythonic way,
# leveraging SQLAlchemy's ORM capabilities.
# Models defined using this Base class will automatically have access to
# features like session management, query capabilities, and more.