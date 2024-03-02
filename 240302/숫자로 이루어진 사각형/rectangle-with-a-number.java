import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        arr(n);


    }

    public static void arr(int n){
        int c = 1;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                System.out.printf("%d ", c);
                c++;
                
                if(c == 10){
                    c = 1;
                    
                }

            }
            System.out.printf("\n");
            
        }

    }

}