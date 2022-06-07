import json
from ..models.audit_log import AuditLog
from datetime import datetime


class AuditObserver:
    def _parse_model(self, model, action):
        """Parse the model to get the table name and primary key.
        Args:
            model (masoniteorm.models.Model): model model.
        """
        new_value = model.__attributes__
        old_value = model.__original_attributes__

        for key in new_value:
            if isinstance(new_value.get(key), datetime):
                new_value[key] = new_value.get(key).to_datetime_string()
            if isinstance(old_value.get(key), datetime):
                old_value[key] = old_value.get(key).to_datetime_string()

        data = {
            "action": action,
            "model_id": model.id,
            "model_name": model.get_table_name(),
            "columns": json.dumps(model.get_columns()),
            "new_value": json.dumps(new_value),
            "old_value": json.dumps(old_value),
        }

        AuditLog.create(data)

    def created(self, model):
        """Handle the model "created" event.
        Args:
            model (masoniteorm.models.Model): model model.
        """
        self._parse_model(model, "CREATED")

    def saved(self, model):
        """Handle the model "saved" event.
        Args:
            model (masoniteorm.models.Model): model model.
        """
        self._parse_model(model, "SAVED")

    def updated(self, model):
        """Handle the model "updated" event.
        Args:
            model (masoniteorm.models.Model): model model.
        """
        self._parse_model(model, "UPDATED")

    def deleted(self, model):
        """Handle the model "deleted" event.
        Args:
            model (masoniteorm.models.Model): model model.
        """
        self._parse_model(model, "DELETED")
