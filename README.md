# Telegram Media Downloader (telegram-dl)
### Download media from Telegram


## installation

### manual process
`git clone https://github.com/rsanjuan87/telegram-dl && cd telegram-dl && ./install.sh`

## uninstallation

### manual process
`git clone https://github.com/rsanjuan87/telegram-dl && cd telegram-dl && ./uninstall.sh && cd .. && rm -rf telegram-dl`

## usage
`telegram-dl https://t.me/chat_id/874 ~/` 

## simple usage
`telegram-dl https://t.me/chat_id/874`


## all params
    Usage: telegram-dl <url> [output dir]
    Options:
     session options
      -n, --phone-number=<phone number> Session phone number to use
    
     collision options
      -o, --on-collision-overwrite      Overwrite existing files
      -r, --on-collision-rename         Rename existing files
      -c, --on-collision-cancel         Cancel existing files

     progress options
      -l, --progress-log                Show progress as log
      -b, --progress-bar                Show progress as bar

     basic options
      -q, --quiet                       Quiet mode
      -h, --help                        Show this help
