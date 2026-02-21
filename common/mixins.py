class FilteringMixin:
    filter_fields = {}

    def get_queryset(self):
        q_set = super().get_queryset()

        for param, lookup in self.filter_fields.items():
            value = self.request.GET.get(param)
            if value:
                kwargs = {lookup: value}
                q_set = q_set.filter(**kwargs)

        return q_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filters = {}
        for param in self.filter_fields:
            filters[param] = self.request.GET.get(param, '')
        context['filters'] = filters

        return context
