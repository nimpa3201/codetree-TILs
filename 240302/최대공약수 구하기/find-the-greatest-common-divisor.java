import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        arr(n, m);


    }

    public static void arr(int a, int b){

        int max = 0;

        if(a <= b){

            for(int i = 1; i <= a; i++){
                if( (a % i == 0) && (b % i == 0)){
                    max = i;

                }
            }

        }
        else{
            for(int i = 1; i <= b; i++){
                if( (a % i == 0) && (b % i == 0)){
                    max = i;
                    
                }
            }
        }
        System.out.printf("%d", max);

    }
}