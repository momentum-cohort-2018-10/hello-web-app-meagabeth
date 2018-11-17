from registration.backends.simple.views import RegistrationView

# my new registration view, subclassing registration view from our plugin
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
         # the named url that we want to redirect to after successful registration
         return ('registration_create_entry')