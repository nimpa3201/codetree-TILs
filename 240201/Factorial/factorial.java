import java.util.Scanner;

public class Main {
    public static int arr(int a){
        if(a <= 1){
            return 1;

        }
        return arr(a - 1) * a;

    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        

        
        System.out.printf("%d", arr(n));
        // 여기에 코드를 작성해주세요.
    }
}