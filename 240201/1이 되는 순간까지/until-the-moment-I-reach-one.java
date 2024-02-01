import java.util.Scanner;

public class Main {
    public static int s = 0;
    
    public static int arr(int a){
      
        if(a == 1){
            return s++;

            
        }
        else if(a % 2 == 0){
            arr(a / 2);
            return s++;

        }
        else{
            arr(a /3);
            return s++;

        }
    
        
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        System.out.printf("%d", arr(n));


        // 여기에 코드를 작성해주세요.
    }
}