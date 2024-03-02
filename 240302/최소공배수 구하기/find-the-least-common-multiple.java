import java.util.Scanner;

public class Main{
    public static void main(String[] args){

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        int m = sc.nextInt();


        arr(n, m);


    }

    public static void arr(int n, int m){

        int max = 0;
        int c = 1;


        if(n >= m){
            while(1>0) {
                if(n % m == 0){
                    max = n;
                    break;

                }
                c++;
                n *= c;
            }

        }

        else{
            while(1>0) {
                if(m % n == 0){
                    max = m;
                    break;

                }
                c++;
                m *= c;

            }

        }
        System.out.printf("%d", max);

    }
}