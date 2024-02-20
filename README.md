# Runtime dependencies
Python3 PySide2

# Ubuntu install
```bash
sudo apt-get -y install python3-pyside2.qtwidget chromium-browser python3-selenium
sudo python3 -m pip install webdrivermanager --break-system-pack
```

# dlensExporter
Python GUI program to convert .dlens files from Delver Lens N mobile application into .csv format to allow importing into various sites and platforms. A .csv file will be create for each collection type [LISTS, DECKS, WANT, TRADE] that has each card in the collection.  It will also create a .csv for each folder in the collection.  This is useful to upload decks or all cards at once.

<p align="center">
  <img src="demo.gif" alt="Demo" />
</p>

## Usage
On startup APK database, Scryfall json and dlens backup will be automaticly fectched if none are present.
Delver lens has support to automaticlly backup to dropbox. Creating a shareable link and updating `collectionLink` in ./settings.yaml will automaticlly fecth the dlens file for you.
- NOTE: Updating the URL www.dl.dropboxusercontent.com will download the file rather then the typical page asking the user to download if www.dropbox.com is used.

Three required files can also be manually fetched with:
* data.db from /res/raw/ in Delver Lens N APK, you can obtain this by extracting the APK downloadable for example from https://apkcombo.com/mtg-card-scanner-delver-lens/delverlab.delverlens/.
* .json file with offline card data from Scryfall, downloadable from https://scryfall.com/docs/api/bulk-data, Default Cards should suffice for most cases.
* .dlens file from Delver Lens N through it's backup or export deck option.

## Authors
- [Derek Stiles](https://github.com/KVL314)

Hope this was helpful!