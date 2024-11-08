import java.util.Scanner;

public class Main {

    public static void findGCD(int n, int m){
        int temp;

        if(n > m){
            temp = n;
            n = m;
            m = temp;
        }

        for(int i = n; i > 0; i --){
            if((n % i == 0) && (m % i == 0)){
                System.out.printf("%d", i);
                break;
            }
        }
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        findGCD(n,m);

        // 여기에 코드를 작성해주세요.
    }
}