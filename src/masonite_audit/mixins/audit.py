from ..models.audit_log import AuditLog


class Audit(object):
    def history(self):
        """Returns a list of logs for the model."""
        return (
            AuditLog.where("model_name", self.__class__.get_table_name())
            .where("model_id", self.id)
            .order_by("created_at", "desc")
            .get()
        )

    def rollback(self, step=1):
        """Rolls back a log to the model."""
        logs = self.history()
        if len(logs) >= step:
            log = logs[step - 1]  # because step is index+1
            log.old_value.pop("updated_at")
            self.update(log.old_value)
            self.save()
