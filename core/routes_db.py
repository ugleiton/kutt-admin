class DjangoRouter:

    def db_for_read(self, model, **hints):
        #print("RD{}".format(model._meta.app_label))
        if model._meta.app_label == 'kutt':
            return 'kuttdatabase'
        return None
    
    def db_for_write(self, model, **hints):
        #print("WR{}".format(model._meta.app_label))
        if model._meta.app_label == 'kutt':
            return 'kuttdatabase'
        return None
    
    def allow_migrate(self,db, app_label, model_name=None, **hints):
        #print("DB{}".format(db))
        if db == 'kuttdatabase':
            return app_label == 'kutt'
        elif app_label == 'kutt':
            return False
        return None
    
    def allow_syncdb(self, db, model):
        print("DB{}".format(db))
        if db == 'kuttdatabase':
            return model._meta.app_label == 'kutt'
        elif model._meta.app_label == 'kutt':
            return False
        return None
