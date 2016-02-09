"""
    auto_close
    ~~~~~~~~~~

    A simple plugin that auto closes HTML tags right after '>'.

    Inspired by Geany's HTML auto close functionality.

    :copyright: (c) 2016 by Peter Justin <peter.justin@outlook.com>
    :license: BSD, see LICENSE for more functionality
"""
import sublime_plugin


class AutoCloseTagCommand(sublime_plugin.TextCommand):
    def run(self, edit, prefix=""):
        self.view.run_command('insert', {'characters': prefix})
        cursorPosition = self.view.sel()[0].begin()
        # close the tag
        self.view.run_command('close_tag')
        self.view.sel().clear()
        self.view.sel().add(cursorPosition)
