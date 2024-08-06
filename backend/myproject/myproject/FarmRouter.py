
from schema_testing.models import Agriculturalparcel

ROUTED_MODELS = ['Agriculturalparcel']

class FarmRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'schema_testing':
            return 'farm'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'schema_testing':
            return 'farm'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'schema_testing' or obj2._meta.app_label == 'schema_testing':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'schema_testing':
            return db == 'farm'
        return db == 'default'