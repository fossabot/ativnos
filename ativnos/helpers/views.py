from django.views.generic import CreateView as _CreateView


class CreateView(_CreateView):
    """
    uses 400 response code for invalid form submissions
    """

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(
            self.get_context_data(form=form), status=400)
