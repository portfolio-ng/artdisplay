An interactive zoom display of an artist's work.
Generalised from the initial development commissioned for the Bill Farmer Gallery.


#### Directory Tree
* **dada/** json dada store outputs from scripts/dada.py
* **img/**
  * **dzi/** tiled image dada for openseadragon
  * **data/** openseadragon dada
* **scripts/** collection of python scripts for creating the naive json dada store
*  **web/**  generalised htm,js,css webfiles
  * **billfarmer/** original Bill Farmer Gallery Display
  * **sans/** an html dump style version of the collection sans any extraneous libraries
  * **lib/**
    * **MagickSlicer/** library for tiling images into dzi format for openseadragon   License: MIT
    * **openseadragon/** FOSS image tiling software   License: New BSD



#### JSON dada schema
```javascript
[
  "ARTIST_NAME":{
    "works": [
      "title": 'STR: Title of the piece',
      "desc": 'STR: Description of the imagery',
      "tags": 'STR: comma seperated categorical tags',
      "media": 'STR: media used in creating the piece',
      "date": 'STR: Date of production of the piece',
      "location": 'STR: Location of production of the piece',
      "dim": {
        "hei": 'STR: Height and units',
        "wid": 'STR: Width and units',
        "dep": 'STR: Depth and units',
        "wei": 'STR: Weight and units, or key reference'
       }
    ]
  }
]
```
###### Weight Key:
* lsp: Light stock paper
* msp: Medium stock paper
* hsp: Heavy stock paper

#### scripts/base.py commands 
* ref : prints this reference list of commands
* piece : step through all properties of current piece
* title,desc,tags,media,date,.. : modify current property
* search : search the dada for any string
* alltags,allmedia,.. : print example properties currently used in the dada with number of times used

