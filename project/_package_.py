````````
target_name = project + '.py'
````````
import sublime
import sublime_plugin



class {{ ProJect }}Command(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        for region in self.view.sel():
            try:
                error = self.run_each(edit, region, **kwargs)
            except Exception as exception:
                print repr(exception)
                error = exception.message

            if error:
                sublime.status_message(error)

    def run_each(self, edit, region):
        pass

