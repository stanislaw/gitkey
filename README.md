# gitkey

## Installation

1) Download the latest gitkey file:

```
wget https://raw.githubusercontent.com/stanislaw/gitkey/refs/heads/main/gitkey
```

2) Place it to a directory which is known to your PATH, for example:

```
cp gitkey ~/HOME/.local/bin/`.
chmod +x ~/HOME/.local/bin/gitkey
```

3) Register the key binding with your terminal.

Bash:

```bash
export HISTIGNORE="gitkey"
bind '"\C-g":"gitkey\n"'
```
