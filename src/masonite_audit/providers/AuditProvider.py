"""A AuditProvider Service Provider."""

from masonite.packages import PackageProvider

from ..masonite_audit import MasoniteAudit


class AuditProvider(PackageProvider, MasoniteAudit):
    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("masonite_audit")
            .name("masonite-audit")
            .config("config/masonite_audit.py", publish=True)
            .migrations("migrations/create_audit_logs_table.py")
        )

    def register(self):
        super().register()
        self.observe()

    def boot(self):
        """Boots services required by the container."""
        pass
