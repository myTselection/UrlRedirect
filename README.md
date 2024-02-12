# Redirect
Download a file and see all redirects used. This can be useful if some firewall whitelisting is required and all url's in the download will need to be whitelisted.

All redirections used during the download will be appended to file `redirect.txt`.

## Usage

### GUI
`usage Windows GUI: redirect.exe`

`usage Python  GUI: python redirect.py`

### CLI

`usage Windows CLI: redirect.exe [-h] [--loglevel {DEBUG,INFO,WARNING,ERROR}] url filename`

`usage Python  CLI: python redirect.py [-h] [--loglevel {DEBUG,INFO,WARNING,ERROR}] url filename`

Download file and see all redirects used. If no command line arguments are provided, the GUI will be shown to enter the URL and filename. CLI only requires the URL and filename.

```
positional arguments:
  url                   URL of the file to download
  filename              Name of the file to save

options:
  -h, --help            show this help message and exit
  --loglevel {DEBUG,INFO,WARNING,ERROR}
                        Logging level
```

## GUI

![image](https://github.com/myTselection/UrlRedirect/assets/587940/c9540886-68d5-430f-a61d-58a98af325be)


## Installation
Download latest [release](https://github.com/myTselection/UrlRedirect/releases) zip, which contains redirect.exe.
