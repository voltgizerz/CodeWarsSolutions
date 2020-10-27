public class Kata {
    public static String tripleTrouble(String one, String two, String three) {
        String comb = "";
        for (int i=0;i<one.length();i++){
           comb=comb.concat(Character.toString(one.charAt(i))+Character.toString(two.charAt(i))+Character.toString(three.charAt(i)));
        }
        return comb;
    }
  }