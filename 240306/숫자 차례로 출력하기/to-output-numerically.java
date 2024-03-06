import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner sc = new Scanner(System. in);
        int n = sc.nextInt();

        arr1(n);
        System.out.println();

        arr2(n);


    }
    public static void arr1(int n){
        if(n == 0){
            return;

        }

        

        arr1(n -1);
        System.out.printf("%d ", n);

    }
    public static void arr2(int n){
        if(n == 0){
            return;

        }

        System.out.printf("%d ", n);

        arr2(n -1);
        
    }
}