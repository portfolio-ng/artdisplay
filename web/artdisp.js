globes={}

globes["ui"]={
"buttons":1,
"title":1,
"desc":1,
"tags":1,
"media":1,
"date":1,
"location":1,
"dim":{
"hei":1,
"wid":1,
"dep":1,
"wei":1
},
"ledger":1,
"image":1,
"pallette":1,
"back":1
}

globes["curr"]=17  //arbitrary placeholder

function buttonc(dir){
  //dir : STR : direction to move in list : lt|rt  dec|asc
  if (dir == "lt" ){  //list dec
    if (globes["curr"]-1>=0){  //if beginning of list loop to last element
      globes["curr"]=globes["curr"]-1
    } else{
      globes["curr"]=_artist.length-1
    }
  } else {  //list asc
    if ( globes["curr"]+1<_artist.length){  
      globes["curr"]=globes["curr"]+1
    } else {   //if end of list loop to initial element 
      globes["curr"]=0
    }
  }
  //console.log(globes["curr"])  //debug
  fillui(_artist[globes["curr"]])
}
// buttonc(STR), button click loops the images list modularly depending on passed direction


function uic(ui){
  // ui : OBJ : list of ui component paramenters
  var domo=document.createElement("div")
  for (var p in ui) {
    if ( ui[p] == 1 || typeof ui[p]=='object' ){
    var po=document.createElement("p")
    po.id=p
    if ( p == "dim") {
      for ( var d in ui[p] ) {
        if ( ui[p][d] == 1){
          var dop=document.createElement("p")
        dop.id=d
        dop.innerHTML=""
        domo.appendChild(dop)
      }
      }
    }
    else if ( p == "buttons" && ui[p]==1 ){
      var butb=document.createElement("div")
      var pb=document.createElement("button")
      pb.innerHTML="<"
      butb.setAttribute("class","buttons")
      pb.setAttribute("onClick","javascript: buttonc('lt');")
      butb.appendChild(pb)
      domo.appendChild(butb)
      var butf=document.createElement("div")
      var pf=document.createElement("button")
      pf.innerHTML=">"
      pf.setAttribute("onClick","javascript: buttonc('rt');")
      butf.setAttribute("class","buttons")
      butf.appendChild(pf)
      domo.appendChild(butf)
      var block=document.createElement("br")
      domo.appendChild(block)
    }
    else if ( p == "back"){
      var po=document.createElement("p")
      po.id=p
      domo.appendChild(po)
    }
    else if ( p == "image" ) {
      continue
    }
    else {
      po.innerHTML=""
      domo.appendChild(po)
    }
  }
  }
  document.body.appendChild(domo)
}
// uic(OBJ), create the ui using parameters in passed argument



function fillui(obj){
  oid=obj.ledger
  for (var p in obj) {
    var po=document.getElementById(p)
    if ( p == "dim") {
      po=document.createElement("div")
      for ( var d in obj[p] ) {
        var dop=document.getElementById(d)
        dop.innerHTML=d+" : "+obj[p][d]
      }
    }
    else if ( p == "back"){
      po.innerHTML="backObj"
    }
    else if ( p == "image" ) {
      var imgr=obj[p]
      imgr=imgr.substring(0,imgr.length-3)+"dzi"
      viewer.close()
      viewer.open("../dada/img/dzi/"+imgr)
      viewer.isVisible(true)
    }
    else {
      po.innerHTML=p+" : "+obj[p]
    }
  }
  return obj
}


function onit(arc){
  //console.log(arc)
  _artist=arc[1]["bf"]
  uic(globes["ui"])
  fillui(_artist[globes["curr"]])
}
onit(archive)  //archive from dada/data.js file
