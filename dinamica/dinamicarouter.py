class DinamicaRouter:
    """
    A router to control all database operations on models in the
    dinamica application.
    """
    route_app_labels = ('dinamica',)

    def db_for_read(self, model, **hints):
        """
        Attempts to read martins_postgres models go to martins_postgres.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'martins_postgres'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write martins_postgres models go to martins_postgres.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'martins_postgres'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the martins_postgres apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the martins_postgres apps only appear in the
        'martins_postgres' database.
        """
        if app_label in self.route_app_labels:
            return db == 'martins_postgres'
        return None