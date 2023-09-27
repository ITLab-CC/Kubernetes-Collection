# Auto Completion

## Mac ZSH

```bash
brew install bash-completion
echo 'source <(kubectl completion zsh)' >>~/.zshrc
source ~/.zshrc
# Alias
echo 'alias k=kubectl' >>~/.zshrc
```

Now you can use `k` instead of `kubectl`.
And you can use `<TAB>` to auto complete commands.
