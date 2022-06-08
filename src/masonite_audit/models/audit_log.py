from masoniteorm.models import Model


class AuditLog(Model):

    __fillable__ = [
        "editor_id",
        "model_id",
        "model_name",
        "action",
        "columns",
        "old_value",
        "new_value",
        "created_at",
        "updated_at",
    ]

    __casts__ = {
        "columns": "json",
        "old_value": "json",
        "new_value": "json",
    }
