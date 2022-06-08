from masonite.tests import TestCase
from masoniteorm.query import QueryBuilder
from tests.integrations.app.models.User import User
from masonite.facades import Hash


class TestAudit(TestCase):
    @classmethod
    def setUpClass(cls):
        QueryBuilder().table("audit_logs").truncate(True)
        QueryBuilder().table("users").truncate(True)

    def tearDown(self):
        super().tearDown()
        QueryBuilder().table("audit_logs").truncate(True)
        QueryBuilder().table("users").truncate(True)

    def test_audit_created(self):
        user = User.create(
            {
                "name": "Yubaraj",
                "email": "user@example.com",
                "password": Hash.make("secret"),
                "phone": "+123456789",
            }
        )

        self.assertDatabaseHas(
            "users",
            {
                "email": "user@example.com",
            },
        )

        self.assertDatabaseHas(
            "audit_logs",
            {
                "model_id": user.id,
                "model_name": "users",
                "action": "CREATED",
            },
        )
