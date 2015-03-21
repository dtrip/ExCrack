
from cement.core import foundation,handler

import baseController
import ExCrack

class ExCrack:
    def init(self):
        pass

    def run(self):
        try:
            app = foundation.CementApp('ExCrack')

            print("registering classes")
            handler.register(baseController.baseController)
            handler.register(Cracker.Crack)

            app.setup()

            app.run()
        finally:
            app.close()
