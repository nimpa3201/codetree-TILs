import java.util.Scanner;

public class Main {
    public static int[][] arr = new int[201][201];

    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        int whith = 0;

        
        for(int i = 0; i < n; i++){
        
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int d = sc.nextInt();
            a += 100;
            b += 100;
            c += 100;
            d += 100;


            whith = arr(a , b , c , d);
        }

        System.out.printf("%d", whith);


    
     
    }

    public static int arr(int a, int b, int c, int d){
        for(int i = a; i < c; i++){
            for(int j = b; j < d; j++){
                arr[i][j]= 1;
            }
        }

        int q = 0;
        for(int i = 0; i < 201; i++){
            for(int j = 0; j < 201; j++){
                q += arr[i][j];

                //System.out.printf("%d", arr[i][j]);

            }
            

        }

        return q;     
    }
}