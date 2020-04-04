class DinamicaRouter:
    """
    A router to control all database operations on models in the
    dinamica application.
    """
    route_app_labels = ('dinamica',)

    def db_for_read(self, model, **hints):
        """
        Attempts to read pricing_analitica2 models go to pricing_analitica2.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'pricing_analitica2'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write pricing_analitica2 models go to pricing_analitica2.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'pricing_analitica2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the pricing_analitica2 apps is
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
        Make sure the pricing_analitica2 apps only appear in the
        'pricing_analitica2' database.
        """
        if app_label in self.route_app_labels:
            return db == 'pricing_analitica2'
        return None