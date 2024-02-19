# Runtime dependencies
Python3 PySide2

# Ubuntu install
```bash
sudo apt-get -y install python3-pyside2.qtwidget
```

# dlensExporter
Python GUI program to convert .dlens files from Delver Lens N mobile application into .csv format to allow importing into various sites and platforms.

<p align="center">
  <img src="demo.gif" alt="Demo" />
</p>

## Usage

On startup APK database, Scryfall json and dlens backup will be automaticly fectched if none are present.
Delver lens has support to automaticlly backup to dropbox. Creating a shareable link and placing it in ./dropbox.link will automaticlly fecth the dlens file for you.
NOTE: Updating the URL www.dl.dropboxusercontent.com will download the file rather then the typical page asking the user to download if www.dropbox.com is used.

Three required files can also be manually fetched with:
* data.db from /res/raw/ in Delver Lens N APK, you can obtain this by extracting the APK downloadable for example from https://apkcombo.com/mtg-card-scanner-delver-lens/delverlab.delverlens/.
* .json file with offline card data from Scryfall, downloadable from https://scryfall.com/docs/api/bulk-data, Default Cards should suffice for most cases.
* .dlens file from Delver Lens N through it's backup or export deck option.

Clone the repository and install necessary dependecies. Under releases I have included pre-compiled binaries but due to included dependencies they're quite large.

## Notes

* Currently only supports Deckbox .csv format. There are some differences between what Scryfall API provides as card or set names, and some of these are automatically converted. I have added some I've come across myself, but it's not all-inclusive.
