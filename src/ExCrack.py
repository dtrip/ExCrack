
import sys
import os

from cement.core import foundation,handler

sys.path.append(os.getcwd())

import baseController
import Cracker

print("\n__ ExCrack: Excel password protected workbook cracker __\n")
print("Disclaimer: Be good, or be good at it.\n")


class ExCrack:
    def init(self):
        pass

    def run(self):
        try:
            app = foundation.CementApp('ExCrack')

            handler.register(baseController.baseController)
            handler.register(Cracker.Cracker)

            app.setup()

            app.run()
        except Exception as e:
            print("Error: %s" % str(e))
        finally:
            app.close()

e = ExCrack()
e.run()
