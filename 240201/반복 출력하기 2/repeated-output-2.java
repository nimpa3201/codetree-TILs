import java.util.Scanner;

public class Main {

    public static void arr(int a){
        if(a == 0){
            return;

        }
        arr(a - 1);
        System.out.printf("HelloWorld\n");

    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        arr(n);

        // 여기에 코드를 작성해주세요.
    }
}