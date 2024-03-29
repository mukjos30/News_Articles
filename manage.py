from app import createApp
from flask_script import Manager,Server

app = createApp('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
