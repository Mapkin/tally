from tally.api.resources import CountersResource
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(CountersResource())
