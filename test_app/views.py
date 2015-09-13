from django.views.generic import DetailView
from test_app.models import DummyModel, SecondDummyModel
from suggestions.views import update_suggestions_dictionary, get_suggestions
from django.contrib.auth import authenticate, login


class DummyDetailView(DetailView):
    model = DummyModel
    template_name = 'test_app/dummy.html'

    def get_context_data(self, **kwargs):
        user = authenticate(username='user', password='pass')
        if user is not None:
            login(self.request, user)
        context = super(DummyDetailView, self).get_context_data(**kwargs)
        update_suggestions_dictionary(self.request, self.object)
        context["suggestions"] = get_suggestions(self.object)
        return context


class SecondDummyDetailView(DetailView):
    model = SecondDummyModel
    template_name = 'test_app/dummy.html'

    def get_context_data(self, **kwargs):
        user = authenticate(username='user', password='pass')
        if user is not None:
            login(self.request, user)
        context = super(SecondDummyDetailView, self).get_context_data(**kwargs)
        update_suggestions_dictionary(self.request, self.object)
        context["suggestions"] = get_suggestions(self.object)
        return context
