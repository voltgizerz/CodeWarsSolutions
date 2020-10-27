function spongeMeme(sentence) {
    var w = sentence.split("")
    var x =""
    var last = "upper"
    for (i = 0; i < w.length; i++) {
          if(w[i-1] == "" && last =="upper"){
              last="lower"
          }else if(w[i-1] == "" && last =="lower"){
              last ="upper"
          }
          
          if(last =="upper"){
            x = x.concat(w[i].toUpperCase())
            last = "lower"
          }
          else{
            x = x.concat(w[i].toLowerCase())
            last = "upper"
          }
        }
    return x
  }