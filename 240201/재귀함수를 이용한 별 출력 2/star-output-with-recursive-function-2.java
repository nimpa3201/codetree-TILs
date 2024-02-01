import java.util.Scanner;

public class Main {

    public static void arr(int a){
        if(a == 0){
            return;

        }
        for(int i = 0; i < a; i++){
            System.out.printf("* ");

        }
        System.out.printf("\n");

        arr(a -1);
        for(int i = 0; i < a; i++){
            System.out.printf("* ");

        }
        System.out.printf("\n");
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        arr(n);

        // 여기에 코드를 작성해주세요.
    }
}