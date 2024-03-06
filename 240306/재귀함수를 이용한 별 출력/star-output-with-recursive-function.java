import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System. in);
        int n = sc.nextInt();

        arr(n);



    }

    public static void arr(int n){
        if(n == 0){
            return;

        }
        
        arr(n - 1);

        for(int i = 0; i < n; i++){
            System.out.printf("*");

        }
        System.out.printf("\n");

    }


}