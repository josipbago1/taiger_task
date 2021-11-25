import pickle

class DataAccess:

    def get_all_objects(self, model_name):
        return self.get_db_content()[model_name]

    def find_object_by_id(self, obj_id, model_name):
        for obj in self.get_db_content()[model_name]:
            if obj_id == obj.article_id:
                return obj
            else:
                return None

    @staticmethod
    def get_db_content():
        with open('db_content', 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def write_db_content(db_content):
        with open('db_content', 'wb') as file:
            pickle.dump(db_content, file)
