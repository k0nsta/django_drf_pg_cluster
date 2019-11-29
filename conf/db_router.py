

class MasterReplicaDbRouter:

    def db_for_read(self, model, **hints):
        return 'replica'

    def db_for_write(self, model, **hints):
        return 'master'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('master', 'replica', 'default')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, modeusername=None, **hints):
        return True
