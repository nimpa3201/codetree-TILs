import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        int c = 0;

        for(int i = a; i <= b ; i++){
            if(arr(i)){
                c += i;

            }    

        }
        
        System.out.printf("%d", c);
        // 여기에 코드를 작성해주세요.
    }

    public static boolean arr(int n){
        for(int i = 2; i < n; i++){
            if(n % i == 0){
                return false;

            }
       }
        return true; 
    }
}