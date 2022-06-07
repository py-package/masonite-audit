from .observer.audit_observer import AuditObserver


class MasoniteAudit:
    def observe(self):
        from .mixins import Audit

        for model in Audit.__subclasses__():
            model.observe(AuditObserver())
