from rest_framework.schemas import AutoSchema


class RecycleSchema (AutoSchema):
    """
    Overrides 'get_manual_fields()' to provide Custom Behavior X
    """
    
    def __init__(self, manual_fields=None, delete_fields=None):
        """
        Parameters:

        * `manual_fields`: list of `coreapi.Field` instances that
            will be added to auto-generated fields, overwriting on `Field.name`
        """
        super (RecycleSchema, self).__init__ (manual_fields)
        if manual_fields is None:
            manual_fields = []
        self._manual_fields = manual_fields
        if delete_fields is None:
            delete_fields = []
        self._delete_fields = delete_fields
    
    def get_manual_fields(self, path, method):
        """Example adding per-method fields."""
        
        delete_fields = []
        if method == 'DELETE':
            delete_fields = self._delete_fields
        
        manual_fields = super ().get_manual_fields (path, method)
        return manual_fields + delete_fields
    
    def get_delete_fields(self, path, method):
        return self._delete_fields