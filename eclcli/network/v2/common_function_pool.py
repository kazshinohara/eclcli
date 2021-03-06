from eclcli.common import command
from eclcli.common import utils
from ..networkclient.common import utils as to_obj


class ListCommonFunctionPool(command.Lister):
    def get_parser(self, prog_name):
        parser = super(ListCommonFunctionPool, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        network_client = self.app.client_manager.network

        columns = (
            'id',
            'name',
            'description',
        )
        column_headers = (
            'ID',
            'Name',
            'Description',
        )

        data = [to_obj.CommonFunctionPool(cfp)
            for cfp in network_client.list_common_function_pools().get('common_function_pools')]

        return (column_headers,
                (utils.get_item_properties(
                    s, columns,
                ) for s in data))


class ShowCommonFunctionPool(command.ShowOne):
    def get_parser(self, prog_name):
        parser = super(ShowCommonFunctionPool, self).get_parser(prog_name)
        parser.add_argument(
            'common_function_pool_id',
            metavar="COMMON_FUNCTION_ID",
            help="ID of Common Function Pool to show."
        )
        return parser

    def take_action(self, parsed_args):
        network_client = self.app.client_manager.network

        common_function_pool_id = parsed_args.common_function_pool_id

        dic = network_client.show_common_function_pool(common_function_pool_id).get('common_function_pool')
        columns = utils.get_columns(dic)
        obj = to_obj.CommonFunctionPool(dic)
        data = utils.get_item_properties(
            obj, columns,)
        return (columns, data)
