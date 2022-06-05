"""A WelcomeController Module."""
import random
from masonite.views import View
from masonite.controllers import Controller

from tests.integrations.app.models.User import User


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        user = User.first()
        # get random number

        user.update({
            'name': f'John {random.randint(100, 900)}'
        })
        
        return user
        return view.render("welcome", {"user": user})

    def test(self):
        user = User.first()

        return {
            
        }
