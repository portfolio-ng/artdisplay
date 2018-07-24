//onit

function onit(arc){
  console.log(arc)
  bill=arc[1]["bf"]
  for (var i=0;i<bill.length;i++){
    buildObj(bill[i])
  }
}

function buildObj(obj){
  oid=obj.ledger
  ocl="dada"
  var domo=document.createElement("div")
  domo.id=oid
  domo.className=ocl
  for ( var p in obj){
    var po=document.createElement("p")
    po.id=oid
    if ( p == "dim") {
      po=document.createElement("div")
      for ( var d in obj[p] ) {
        var dop=document.createElement("p")
        dop.innerHTML=d+":"+obj[p][d]
        po.appendChild(dop)
      }
    }
    else if ( p == "back"){
      po.innerHTML="backObj"
    }
    else if ( p == "image" ) {
      po=document.createElement("img")
      po.src="./IMG/"+obj[p]
      po.style.height="200px"
      po.style.width="200px"
    }
    else {
      po.innerHTML=obj[p]
    }
    domo.appendChild(po)
  }
  appendObj(domo)
  return obj
}

function appendObj(domo){
  document.body.appendChild(domo)
}  
onit(archive)
