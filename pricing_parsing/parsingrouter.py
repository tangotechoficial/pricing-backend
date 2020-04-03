class ParsingRouter:
    """
    A router to control all database operations on models in the
    pricing_parsing application.
    """
    route_app_labels = ('pricing_parsing',)

    def db_for_read(self, model, **hints):
        """
        Attempts to read pricing_parsing models go to pricing_data_parsing.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'pricing_data_parsing'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write pricing_parsing models go to pricing_data_parsing.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'pricing_data_parsing'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the pricing_parsing apps is
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
        Make sure the pricing_parsing apps only appear in the
        'pricing_data_parsing' database.
        """
        if app_label in self.route_app_labels:
            return db == 'pricing_data_parsing'
        return None