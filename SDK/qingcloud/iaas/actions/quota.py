from SDK.qingcloud.iaas import constants as const
from SDK.qingcloud.misc.utils import filter_out_none


class QuotaAction(object):

    def __init__(self, conn):
        self.conn = conn

    def describe_quotas(self,
                           status=None,
                           owner=None,
                           **ignore):
        """ Describe instances filtered by conditions
        @param instances : the array of IDs of instances
        @param image_id : ID of the image which is used to launch this instance.
        @param instance_type: The instance type.
                              See: https://docs.qingcloud.com/api/common/includes/instance_type.html
        @param status : Status of the instance, including pending, running, stopped, terminated.
        @param verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
        @param search_word: the combined search column.
        @param offset: the starting offset of the returning results.
        @param limit: specify the number of the returning results.
        @param tags : the array of IDs of tags.
        """
        action = const.ACTION_DESCRIBE_QUOTAS
        valid_keys = ['status',
                      'verbose']
        body = filter_out_none(locals(), valid_keys)
        if not self.conn.req_checker.check_params(body,
                                                  required_params=[],
                                                  integer_params=[
                                                       'verbose'],
                                                  list_params=[
                                                       'status']
                                                  ):
            return None

        return self.conn.send_request(action, body)



    def get_quota_left(self,
                        **ignore):

        action = const.ACTION_GET_QUOTA_LEFT
        valid_keys = []
        body = filter_out_none (locals (), valid_keys)
        if not self.conn.req_checker.check_params (body,
                                                   required_params=[],
                                                   integer_params=[],
                                                   list_params=[]
                                                   ):
            return None

        return self.conn.send_request (action, body)