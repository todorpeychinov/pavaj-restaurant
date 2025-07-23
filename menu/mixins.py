class UserTrackedMixin:
    def form_valid(self, form):
        if not form.instance.pk:
            form.instance.user_created = self.request.user

        form.instance.last_user_edited = self.request.user

        return super().form_valid(form)
