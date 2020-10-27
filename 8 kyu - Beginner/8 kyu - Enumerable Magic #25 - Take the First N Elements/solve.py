def take(arr,n):
    return arr[0:n]

# JAVA VERSION
# import java.util.Arrays;
# public class ZywOo {
#   public static int[] take(int[] arr, int n) {
#       if (arr.length==0){
#           int[] temp = {};
#           return  temp;
#       }else if (n>arr.length){
#           return arr;
#         }else{
#           return Arrays.copyOfRange(arr, 0, n);
#       }
#   }
# }