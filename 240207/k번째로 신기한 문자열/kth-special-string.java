import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        String T = sc.next();

        String[] arr = new String[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.next();
        }
        String[] arr2 = new String[n];
        
        int s = 0;
        for(int i = 0; i < n; i++){
            int c = 0;    
            for(int j = 0; j < T.length(); j++){
                if(T.charAt(j) == arr[i].charAt(j)){
                    c++;
                

                }
                else{
                    continue;

                }

            }
            if(c == T.length()){
                arr2[i] = arr[i];

            }
            else{
                arr2[i] = "z";

            }
            

        }
       

    

        Arrays.sort(arr2);



        System.out.printf("%s", arr2[k-1]);



        // 여기에 코드를 작성해주세요.
    }
}