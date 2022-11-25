class MiApp2Router:
    """
    A router to control all database operations on models in the
    auth application.
    """
    router_app_labels = {'quiz'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read quiz models go to mongodb.
        """
        if model._meta.app_label in self.router_app_labels:
            return 'mongodb'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write quiz models go to mongodb.
        """
        if model._meta.app_label in self.router_app_labels:
            return 'mongodb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the quiz app is involved.
        """
        if obj1._meta.app_label in self.router_app_labels or \
           obj2._meta.app_label in self.router_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the quiz app only appears in the 'mongodb'
        database.
        """
        if app_label in self.router_app_labels:
            return db == 'mongodb'
        return None
