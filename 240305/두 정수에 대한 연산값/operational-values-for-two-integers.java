import java.util.Scanner;

public class Main{
    public static void main(String[] args){

        Scanner sc = new Scanner(System. in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        arr(a, b);


    }

    public static void arr(int a, int b){
        if(a > b){
            System.out.printf("%d %d", a + 25, b * 2);

        }
        else{
            System.out.printf("%d %d", a * 2, b + 25);

        }
    }
}