import java.util.Scanner;

public class Main{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        System.out.printf("%d", arr(a, b, c));




    }

    public static int arr(int a, int b, int c){
        if(a < b){
            if(a < c ){
                return a;

            }
            else{
                return c;
            }

        }
        else{
            if(b < c){
                return b;
            }
            else{
                return c;

            }
        }
    }
}