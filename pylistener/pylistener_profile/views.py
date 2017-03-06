from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.


class ManageView(LoginRequiredMixin, TemplateView):
    """View for user's management page."""

    template_name = "imager_images/library.html"
    login_url = reverse_lazy("login")

    def get_context_data(self):
        """Get required context data for manage view."""


        return {"addresses": addresses, "categories": categories, "attributes": attribtues}