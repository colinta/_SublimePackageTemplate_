````````
target_name = project + '.py'
````````
import sublime
import sublime_plugin


class {{ Project }}Command(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        e = self.view.begin_edit('{{ project }}')
        regions = [region for region in self.view.sel()]

        # any edits that are performed will happen in reverse; this makes it
        # easy to keep region.a and region.b pointing to the correct locations
        def compare(region_a, region_b):
            return cmp(region_b.end(), region_a.end())
        regions.sort(compare)

        for region in regions:
            error = self.run_each(edit, region, **kwargs)
            if error:
                sublime.status_message(error)
        self.view.end_edit(e)

    def run_each(self, edit, region):
        pass

