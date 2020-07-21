//These are your super secret characters you will use to make the password super secure
var superSecretChars = [['a', '@'],['s', '$'],['o', '0'], ['h', '5'], ['x', '*']];
function createSSP(password){
  return password.split("a").join("@").split("s").join("$").split("o").join("0").split("h").join("5").split("x").join("*").split("A").join("@").split("S").join("$").split("O").join("0").split("H").join("5").split("X").join("*")
}