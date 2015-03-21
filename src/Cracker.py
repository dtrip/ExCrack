
from cement.core import controller

class Cracker(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'Cracker'
        description = 'Object that performs cracking'
        stacked_on = 'base'


    def default(self):
        pass

    # @controller.expose(help='Crack Microsoft Excel file')
    def cracker(self):

        if (self.app.pargs.verbose):
            print("Cracker is starting")

        if (self.app.pargs.file):
            print("No Excel file provided, exiting...")
            exit

        return True
