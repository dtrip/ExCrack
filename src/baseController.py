
from cement.core import controller

class baseController(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'base'
        description = 'Excel Password Cracking'

        config_defaults = {}

        arguments = [
                (['-p', '--passwords'], dict(action='store', help='path/to/passwords.txt')),
                (['-f', '--file'], dict(action='store', help='Excel (.xlsx, or .xls) file')),
                (['-v', '--verbose'], dict(action='store_true', help='Verbose Output'))
                ]

        @controller.expose(hide=True, aliases=['run'])
        def default(self):
            print("Try 'ExCrack --help' for more information")
