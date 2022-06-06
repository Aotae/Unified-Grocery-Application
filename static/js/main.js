const storeArray = []

function storeLst(click){
  if(storeArray.includes(click)){
    const index = storeArray.indexOf(click);
    storeArray.splice(index, 1);
  }
  else{
    storeArray.push(click);
  }
  console.log(storeArray);
}
