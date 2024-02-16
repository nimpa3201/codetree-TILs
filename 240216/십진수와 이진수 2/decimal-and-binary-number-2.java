import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        String n = sc.next();

        int a = 0;

        for(int i = 0; i < n.length(); i++){
            a = a * 2 + (n.charAt(i) - '0');
        }
        a *= 17;

        int[] arr = new int[20];
        int c = 0;

        while(true){
            if(a < 2){
                arr[c++] = a%2;

                break;
            }
            
            arr[c++] = a%2;
            a /= 2;

        }


        for(int i = c-1; i >= 0; i--){
            System.out.printf("%d", arr[i]);
        }           

        


    
        
        // 여기에 코드를 작성해주세요.
    }
}