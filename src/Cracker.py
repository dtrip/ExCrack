

class Cracker(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'Cracker'
        description = 'Object that performs cracking'
        stacked_on = 'base'


    def default(self):
        pass

    @controller.expose(help='Crack Microsoft Excel file')
    def crack(self):

        if (self.app.pargs.verbose):
            print("Cracker is starting")

        return True
