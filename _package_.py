import sublime
import sublime_plugin


class _PACKAGE_Command(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        e = self.view.begin_edit('_package_')
        regions = [region for region in self.view.sel()]

        # any edits that are performed will happen in reverse; this makes it
        # easy to keep region.a and region.b pointing to the correct locations
        def compare(region_a, region_b):
            return cmp(region_b.end(), region_a.end())
        regions.sort(compare)

        for region in regions:
            self.run_each(edit, region, **kwargs)
        self.view.end_edit(e)

    def run_each(self, edit, region):
        pass
