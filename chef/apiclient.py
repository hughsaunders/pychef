from chef.base import ChefObject

class ApiClient(ChefObject):
    """A Chef API Client object."""

    url = '/clients'
    attributes = {
        'admin': bool,
        'name': str,
        'private_key': str
    }
