import json


class AuditObserver:

    def _parse_model(self, model, action):
        """Parse the model to get the table name and primary key.
        Args:
            model (masoniteorm.models.Model): model model.
        """

        return {
            'action': action,
            'model_id': model.id,
            'model_name': model.get_table_name(),
            'columns': json.dumps(model.get_columns()),
            'new_value': model.serialize(),
            'old_value': model.get_dirty_attributes(),
            # 'old_value': model.get_original('name')
        }
    
    def created(self, model):
        """Handle the model "created" event.
        Args:
            model (masoniteorm.models.Model): model model.
        """
        print(self._parse_model(model, 'CREATED'))

    def saved(self, model):
        """Handle the model "saved" event.
        Args:
            model (masoniteorm.models.Model): model model.
        """
        print(self._parse_model(model, 'SAVED'))

    # def updating(self, model):
    #     """Handle the model "updating" event.
    #     Args:
    #         model (masoniteorm.models.Model): model model.
    #     """
    #     print('========================UPDATING========================')
    #     print(model.get_dirty_attributes())

    def updated(self, model):
        """Handle the model "updated" event.
        Args:
            model (masoniteorm.models.Model): model model.
        """
        print('========================UPDATED========================')
        print(self._parse_model(model, 'UPDATED'))

    def deleted(self, model):
        """Handle the model "deleted" event.
        Args:
            model (masoniteorm.models.Model): model model.
        """
        print(self._parse_model(model, 'DELETED'))