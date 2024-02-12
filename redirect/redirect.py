import argparse
import requests
import logging
from gooey import Gooey, GooeyParser
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
      else:
        # Log redirect
        _LOGGER.debug(f"response: {response.status_code}, url: {response.next.url}")
        redirects.append(f"{url} -> {response.next.url}")
        url = response.next.url
    except Exception as e:
      _LOGGER.error(f"Error downloading file: {e}")
      break

  if redirects:
    _LOGGER.debug(f"Redirects occurred:")
    print(f"Redirects occurred:")
    for redirect in redirects:
      _LOGGER.debug(f"Redirect: {redirect}")
      print(f"- {redirect}")


@Gooey
def main():
    import argparse
    parser = GooeyParser(
    # parser = argparse.ArgumentParser(
        description='''
Download a file from URL
''')
    parser.add_argument("url", type=str, help="URL of the file to download")
    parser.add_argument("filename", type=str, help="Name of the file to save", widget="FileSaver")
    parser.add_argument("--loglevel", type=str, choices=["DEBUG", "INFO", "WARNING", "ERROR"], default="INFO", widget="Dropdown", help="Logging level")
    # parser.add_argument("allow_redirect", type=bool, help="Allow redirects", widget='BlockCheckbox')
    args = parser.parse_args()

    _LOGGER.setLevel(args.loglevel)

    ch = logging.StreamHandler()
    ch.setLevel(args.loglevel)

    form = logging.Formatter('%(asctime)s %(message)s',
                             datefmt='%m/%d/%Y %I:%M:%S')

    ch.setFormatter(form)
    _LOGGER.addHandler(ch)

    download_file(args.url, args.filename)

    _LOGGER.debug('done')
    print("done")

if __name__ == '__main__':
    main()
  # _LOGGER.setLevel(logging.DEBUG)
  # ch = logging.StreamHandler()
  # ch.setLevel(logging.DEBUG)

  # form = logging.Formatter('%(asctime)s %(message)s',
  #                         datefmt='%m/%d/%Y %I:%M:%S')

  # ch.setFormatter(form)
  # _LOGGER.addHandler(ch)
  # download_file("https://updates.jenkins.io/download/plugins/pipeline-model-definition/2.2150.v4cfd8916915c/pipeline-model-definition.hpi", "test.txt")

