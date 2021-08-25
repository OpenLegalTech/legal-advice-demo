from django.contrib.auth.mixins import UserPassesTestMixin


class AllowAccessToAdminToEveryonaMixin(UserPassesTestMixin):
    def test_func(self):
        return True
