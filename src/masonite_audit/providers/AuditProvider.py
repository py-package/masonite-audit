"""A AuditProvider Service Provider."""

from masonite.packages import PackageProvider

from ..masonite_audit import MasoniteAudit

class AuditProvider(PackageProvider, MasoniteAudit):
    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("masonite_audit")
            .name("masonite_audit")
            .config("config/masonite_audit.py", publish=True)
        )

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        
        self.observe()
