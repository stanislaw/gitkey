# gitkey

`gitkey` is a small Python script that lets you run Git commands using hotkeys.
It makes Git faster and easier to use, so you do not have to type long commands
all the time. With gitkey, many Git operations go from `O(N)` keystrokes to
`O(1)` keystrokes: one to activate gitkey and one to run a Git command.

To use it, the script needs to be integrated into your favorite shell using key
bindings.

The script itself is very simple and non-industrial. Adding unit/integration and
end-to-end tests, and refactoring it into a better design, would be good future
work. Even without that, the script already does its job well and saves a lot of
effort.

## gitkey command reference

🔥 indicates multi-step "combo" key sequences that run several Git commands and
greatly reduce mental effort.

| Key / Shortcut       | Action                                                |
|----------------------|-------------------------------------------------------|
| `A`                  | `git add .`                                       |
| `B`                  | `git for-each-ref ...` (show latest branches)         |
| `C`                  | `git commit`                                          |
| `D`                  | `git diff`                                            |
| `F`                  | `git fetch`                                           |
| `H`                  | `git show`                                            |
| `L`                  | `git log`                                             |
| `M`                  | `git switch main`                                     |
| `N`                  | `git checkout <new_branch>` - promts a branch name.   |
| `O`                  | `git checkout <branch>` - take branch from buffer     |
| `S`                  | `git status`                                          |
| `W`                  | `git commit -m "WIP`                                  |
| `8`                  | `git reset HEAD^ --hard`                              |
| `9`                  | `git reset HEAD^`                                     |
| `0`                  | `git reset`                                           |
| `!` 🔥               | `git reset --hard`, preserving the diff in a tmp dir. |
| `+` 🔥               | `git add . && git commit --amend --no-edit`           |
| `=` 🔥               | `git add --update . && git commit --amend --no-edit`  |
| `Left      `         | `git switch -`                                        |
| `Shift+Left`         | `git rebase --abort`                                  |
| `Right` 🔥           | `git checkout $(fzf)` - Switch to branch from GUI     |
| `Shift+Right`        | `git rebase --continue`                               |
| `Up`                 | `git push`                                            |
| `Shift+Up`           | `git push --force`                                    |
| `Down`               | `git pull`                                            |
| `Shift+Down`         | `git pull --rebase`                                   |
| `TAB` 🔥             | `git fetch origin && git rebase origin/main`          |
| `Shift+TAB` 🔥       | `git fetch origin && git rebase origin/main -i`       |
| `Delete`             | `git rm --cached <file> && git commit --amend --no-edit` |
| `[`                  | `git stash`                                           |
| `{`                  | `git stash --include-untracked`                       |
| `]`                  | `git stash pop`                                       |
| `}`                  | `git stash show --include-untracked`                  |
| `bl1`                | Currently vacant. Moved to `B`.                       |
| `bl2`                | The same as `B` but also shows the remote branches.   |
| `cm1`                | Currently vacant. Moved to `C`.                       |
| `cm2`                | `git commit --amend`                                  |
| `cm3`                | `git commit --amend --no-edit` (`+` without `add`).   |
| `di1`                | Currently vacant. Moved to `D`.                       |
| `di2`                | `git diff HEAD`                                       |

## Installation

### System requirements

`gitkey` has been tested and works on Linux (Ubuntu) and macOS.

- On Linux, `Shift+O` uses `xclip` for pasting from a copy-and-paste buffer.
- On Linux and macOS, the `Right` key uses `fzf` for selecting a Git branch from a GUI.

Instructions for macOS:

```bash
brew install fzf
```

Instructions for Ubuntu:

```bash
sudo apt install -y xclip fzf
```

### Download the latest gitkey file

```
wget https://raw.githubusercontent.com/stanislaw/gitkey/refs/heads/main/gitkey
```

Place it to a directory which is known to your `PATH`, for example:

```bash
cp gitkey ~/.local/bin/
chmod +x ~/.local/bin/gitkey
```

### Register the key binding with your terminal

#### Bash

```bash
# Append gitkey to HISTIGNORE without removing existing entries
export HISTIGNORE="${HISTIGNORE:+$HISTIGNORE:}gitkey"

# Bind a hotkey.
bind '"\C-g":"gitkey\n"'
```

This will bind gitkey to the `Ctrl+G` key combination. Setting `HISTIGNORE=`
ensures that gitkey is not recorded in the Bash history, keeping your history
free from repeated invocations.

## Contributing

If you like the idea, you can help make gitkey better by:

- Adding instructions for other shells (Zsh, Fish, etc.) or platforms.
- Suggesting or adding new hotkey combinations.
- Improving customization or overall usability.
