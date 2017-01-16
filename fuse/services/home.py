from __future__ import absolute_import, division, print_function, unicode_literals
from fuse.services import Service
import os

class Home(Service):

    def collect(self):

        directory = self.prompt(
            'directory',
            text="Project Home",
            default=os.getcwd(),
            pre_validation_hook=os.path.expanduser
        )

        self.config['directory'] = directory = os.path.expanduser(directory)

        self.send_message('current_working_directory', payload=directory)
