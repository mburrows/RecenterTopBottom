# RecenterTopBottom

A [Sublime Text 2][ST2] plugin that cycles between moving the current line to the top, middle and bottom of the visible screen area.

## Installation

1. Open the Sublime Text 2 Packages folder:

    - OS X: `~/Library/Application Support/Sublime Text 2/Packages/`
    - Windows: `%APPDATA%/Sublime Text 2/Packages/`
    - Linux: `~/.Sublime Text 2/Packages/`

2. Clone this repo:
<pre>
git clone git://github.com/mburrows/RecenterTopBottom.git
</pre>

## Commands

This plugin provides a single command called `recenter_top_bottom`. Repeated calls to this command will move the current line to the top, middle and bottom of the visible screen area. The ordering can be customised using the settings file.

## Keybindings

The default keybinding is similar to `ctrl+l` which is bound to the built in `show_at_center` command:

    { "keys": ["ctrl+alt+l"], "command": "recenter_top_bottom" }

Personally I override the `show_at_center` command with `recenter_top_bottom`, it provides all the functionality of the original command and more. This can be accomplished by putting the following in your `Key Bindings - User` file:

    { "keys": ["ctrl+l"], "command": "recenter_top_bottom" }

## Settings

To change the ordering create a file called `Packages/User/RecenterTopBottom.sublime-settings` and redefine the `recenter_positions` setting as follows:

    {
        "recenter_positions": ["middle", "top", "bottom"]
    }

[ST2]: http://www.sublimetext.com/2