import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        String A = sc.next();
        String B = sc.next();

        int sA = A.length();
        int sB = B.length();



        
        char[] arrA = A.toCharArray();
        Arrays.sort(arrA);
        
        char[] arrB = B.toCharArray();
        Arrays.sort(arrB);
        
        boolean c = true;

        if(sA == sB){
            for(int i = 0; i < sA; i++){
                if(arrA[i] == arrB[i]){
                    
                }
                else{
                    c = false;

                }
            }
        }
        else{
            c = false;

        }

        if(c){
            System.out.printf("Yes");

        }
        else{
            System.out.printf("No");

        }
        // 여기에 코드를 작성해주세요.
    }
}