import java.util.Scanner;

public class Main{
    public static void main(String[] args){

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        int m = sc.nextInt();


        arr(n, m);


    }

    public static void arr(int n, int m){
        int c = 0;

        if(n >= m){
            c = n;

        }
        else{
            c = m;

        }
        int max = 0;
        int q = 1;


        while(true){
            if((c % n == 0) && (c % m == 0)){
                max = c;
                break;

            } 

            c++;
            

        }

        
        System.out.printf("%d", max);

    }
}