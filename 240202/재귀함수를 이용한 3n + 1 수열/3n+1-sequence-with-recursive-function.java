import java.util.Scanner;

public class Main {
    public static int s = 0;

    public static int arr(int n){

        if(n == 1){
            return s += 0; 
        }

        if(n % 2 == 0){
            n /= 2;
            return arr(n) + 1;
        }
        else{
            n = n * 3 + 1;
            return arr(n) + 1;
        }

        
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        System.out.printf("%d",arr(n));

        // 여기에 코드를 작성해주세요.
    }
}