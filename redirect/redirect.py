import requests
import logging
import sys
import argparse
# from gooey import Gooey, GooeyParser
# pip install gooey

_LOGGER = logging.getLogger(__name__)
def download_file(url, filename):
  """Downloads a file from the given URL and saves it as the specified filename.

  Args:
    url: The URL of the file to download.
    filename: The name of the file to save to.
  """
  redirects = []
  while url:
    try:
      response = requests.get(url, stream=True, allow_redirects=False)
      _LOGGER.debug(f"response: {response.status_code}, url: {response.url}")
      if response.status_code == 200:
        with open(filename, 'wb') as f:
          for chunk in response.iter_content(1024):
            if chunk:  # filter out keep-alive new chunks
              f.write(chunk)
        _LOGGER.debug(f"Downloaded file {filename} successfully!")
        print(f"Downloaded file {filename} successfully!")
        break
      elif response.status_code == 302:
        # Log redirect
        _LOGGER.debug(f"response: {response.status_code}, url: {response.next.url}")
        redirects.append(f"{url} -> {response.next.url}")
        url = response.next.url
      else:
        _LOGGER.error(f"Error downloading file: {e}")
    except Exception as e:
      _LOGGER.error(f"Error downloading file: {e}")
      break

  if redirects:
    # Open a file in append mode
    with open('redirects.txt', 'a') as f:
      # Write text to the file
      f.write("Redirects occurred:\n")
      _LOGGER.debug(f"Redirects occurred:")
      print(f"Redirects occurred:")
      for redirect in redirects:
        f.write(f"Redirect: {redirect}\n")
        _LOGGER.debug(f"Redirect: {redirect}")
        print(f"- {redirect}")
    
    print(f"Redirect info added in 'redirects.txt'.")


try:
    import gooey
except ImportError:
    gooey = None


def flex_add_argument(f):
    '''Make the add_argument accept (and ignore) the widget option.'''

    def f_decorated(*args, **kwargs):
        kwargs.pop('widget', None)
        return f(*args, **kwargs)

    return f_decorated


# Monkey-patching a private class…
argparse._ActionsContainer.add_argument = flex_add_argument(argparse.ArgumentParser.add_argument)

# Do not run GUI if it is not available or if command-line arguments are given.
if gooey is None or len(sys.argv) > 1:
    ArgumentParser = argparse.ArgumentParser

    def gui_decorator(f):
        return f
else:
    ArgumentParser = gooey.GooeyParser
    gui_decorator = gooey.Gooey(
        program_name='Redirect',
        # navigation='TABBED',
        suppress_gooey_flag=True,
    )


@gui_decorator
def main():
    _LOGGER.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    form = logging.Formatter('%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S')

    ch.setFormatter(form)
    _LOGGER.addHandler(ch)
    parser = ArgumentParser(description='''
Download file and see all redirects used.
If no command line arguments are provided, the GUI will be shown to enter the URL and filename.
CLI only requires the URL and filename.
''')
    

    parser.add_argument("url", type=str, help="URL of the file to download")
    parser.add_argument("filename", type=str, help="Name of the file to save", widget="FileSaver")
    parser.add_argument("--loglevel", type=str, choices=["DEBUG", "INFO", "WARNING", "ERROR"], default="INFO", widget="Dropdown", help="Logging level")
    # parser.add_argument("allow_redirect", type=bool, help="Allow redirects", widget='BlockCheckbox')
    args = parser.parse_args()

    _LOGGER.setLevel(args.loglevel)
    args = parser.parse_args()
    if args.url and args.filename:
        download_file(args.url, args.filename)
    else:
        print("Both URL and filename are required.")

if __name__ == '__main__':
    main()
  # download_file("https://updates.jenkins.io/download/plugins/pipeline-model-definition/2.2150.v4cfd8916915c/pipeline-model-definition.hpi", "test.txt")

