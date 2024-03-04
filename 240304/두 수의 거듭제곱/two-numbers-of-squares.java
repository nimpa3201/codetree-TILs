import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.printf("%d", arr(a, b));
        // 여기에 코드를 작성해주세요.
    }

    public static int arr(int a, int b){
        int c = 1;

        for(int i = 0; i < b; i++){
            c *= a;

        }
        return c;

    }
}