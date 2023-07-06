# telegram-dl
Telegram Media Downloader

## usage
`python main.py https://t.me/chat_id/874 ~/` 

## simple usage
`python main.py https://t.me/chat_id/874`


## all params
    Usage: telegram-dl <url> [output dir]
    Options:
     session options
      -n, --phone-number=<phone number>\tSession phone number to use
    
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
