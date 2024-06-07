from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect

class IsStaffMixin(UserPassesTestMixin):

    def test_func(self) -> bool:
        return self.request.user.is_staff if self.request.user.is_authenticated else False

    """Verify that the current user has staff status."""
    def handle_no_permission(self, request):
        messages.add_message(request, messages.ERROR, "You need higher permissions in order to access this page.")
        return redirect("competition:list")
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, "You need to be logged in in order to access this page.")
            return redirect("account_login")
        if not request.user.is_staff:
            return self.handle_no_permission(request)
        return super().dispatch(request, *args, **kwargs)