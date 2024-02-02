import java.util.Scanner;

public class Main {
    public static int arr(int d){

        if(d < 10){
            return d;

        }
        return arr(d / 10) + d % 10;
        
    }
    public static void main(String[] args) {


        Scanner sc = new Scanner(System. in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int d = a*b*c;

        System.out.printf("%d", arr(d));

        // 여기에 코드를 작성해주세요.
    }
}