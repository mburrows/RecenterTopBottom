import sublime
import sublime_plugin
from itertools import cycle

settings = sublime.load_settings('RecenterTopBottom.sublime-settings')


class Pref:
    def load(self):
        Pref.positions = settings.get('recenter_positions', ['top', 'middle', 'bottom'])
Pref = Pref()
Pref.load()
settings.add_on_change('reload', lambda: Pref.load())


POSNS = cycle(Pref.positions)


class CaretWatcher(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        # caret has moved, reset positions to their default value
        global POSNS
        POSNS = cycle(Pref.positions)


class RecenterTopBottomCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        posn = next(POSNS)
        if posn == 'top':
            self.show_at_top()
        elif posn == 'bottom':
            self.show_at_bottom()
        else:
            self.view.run_command('show_at_center')

    def row(self):
        caret = self.view.sel()[0].begin()
        return self.view.rowcol(caret)[0]

    def show_at_top(self):
        top, _ = self.screen_extents()
        offset = self.row() - top - 1
        self.view.run_command('scroll_lines', {'amount': -offset})

    def show_at_bottom(self):
        _, bottom = self.screen_extents()
        offset = bottom - self.row() - 1
        self.view.run_command('scroll_lines', {'amount': offset})

    def screen_extents(self):
        screenful = self.view.visible_region()
        top_row, _ = self.view.rowcol(screenful.begin())
        bottom_row, _ = self.view.rowcol(screenful.end())
        return (top_row, bottom_row)
