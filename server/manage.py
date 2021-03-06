import os
import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, get_app, create_app
from app.models import availability, comment, meal, ticket, ticket_history, user

config = os.getenv('APP_SETTINGS') or 'development'

# initialize the app with all its configurations
app = get_app(create_app)(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app/data.db'
migrate = Migrate(app, db)
# create an instance of class that will handle our commands
manager = Manager(app)

# Define the migration command to always be preceded by the word "db"
# Example usage: python manage.py db init
manager.add_command('db', MigrateCommand)


# define our command for testing called "test"
# Usage: python manage.py test
@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('./tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
