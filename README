# **Directory Tree**
  ## dada/
    json dada store outputs from scripts/dada.py
    ### img/
      #### dzi/
        tiled image dada for openseadragon
      #### dada/
        openseadragon dada
  ## scripts/
    collection of python scripts for creating the naive json dada store
  ## web/
    htm,js,css webfiles
    ### lib/
      #### MagickSlicer/
        library for tiling images into dzi format for openseadragon
          License: MIT
      #### openseadragon/
        OSS version of image tiling software
          License: New BSD
    ### sans/
      an html dump style version of the collection sans any extraneous libraries



# ** JSON dada schema **
  artiste[]
    __'ARTIST NAME'{}
      works[]
        title""
          __'Title of the piece'
        desc""
          __'Description of the imagery'
        tags""
          __'comma seperated categorical tags'
        media""
          __'media used in creating the piece'
        date""
          __'Date of production of the piece'
        location""
          __'Location of production of the piece'
        dim{}
          hei
            __'Height'
          wid
            __'Width'
          dep
            __'Depth'
          wei
            __'Weight'
                lsp: light stock paper
                msp: medium stock paper
                hsp: heavy stock paper
  ### types:
    [] list
    {} dict
    "" string

# **scripts/base.py commands **
  ## ref
    prints this reference list of commands
  ## piece
    step through all properties of current piece
  ## title,desc,tags,media,date,..
    modify current property
  ## search
    search the data for any string
  ## alltags,allmedia,..
    print example properties currently used in the data with number of times used

