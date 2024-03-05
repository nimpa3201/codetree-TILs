import java.util.Scanner;

public class Main {
    public static void main(String[] agrs){

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        arr(n);


    }

    public static void arr(int n){

        if(n == 0){
            return;
        }
        System.out.printf("HelloWorld\n");
        arr(n - 1);
        

        
        
    }

}