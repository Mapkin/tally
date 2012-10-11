from django.conf.urls import url
from tally.api.auth import ClientAuthentication
from tally.api.models import Counter
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

import logging


logger = logging.getLogger(__name__)


class CountersResource(ModelResource):
    class Meta:
        queryset = Counter.objects.all()
        resource_name = 'counters'
        authentication = BasicAuthentication(backend=ClientAuthentication(),
                                             realm='tally')
        authorization = Authorization()
        include_resource_uri = False
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get', 'patch', 'put']
        
    def override_urls(self):
        return [
            url(r'^(?P<resource_name>{0})/(?P<name>[\w\d_.-]+)/?$'.
                format(self._meta.resource_name),
                self.wrap_view('dispatch_detail'),
                name="api_dispatch_detail")
        ]

    def obj_update(self, bundle, **kwargs):
        counter = Counter.objects.get(pk=kwargs['pk'])
        counter.increment()
        counter.save()

    def deserialize(self, request, data, format='application/json'):
        if request.method == 'PATCH':
            return {}
        super(CountersResource, self).deserialize(request, data, format)

    def alter_list_data_to_serialize(self, request, data):
        final = []
        for bundle in data['objects']:
            fields = bundle.data
            final.append({
                'id': fields['id'],
                'name': fields['name'],
                'count': fields['count'],
            })
        return final
