class MyAppRouter(object):
    """A router to control all database operations on models in
    the myapp application"""

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'legacy':
            return 'olddata'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'legacy':
            return 'olddata'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_syncdb(self, db, model):
        "Make sure the myapp app only appears on the 'other' db"
        if db == 'olddata':
            return False
        else:
            return True
