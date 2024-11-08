import java.util.Scanner;

public class Main {
    public static int add(int n){
        int sum =0;

        for(int i = 1; i <= n; i++){
            sum += i;
        }
        return sum / 10;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        System.out.printf("%d", add(n));

        // 여기에 코드를 작성해주세요.
    }
}