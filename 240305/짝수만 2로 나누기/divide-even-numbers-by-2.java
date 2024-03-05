import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
            //System.out.printf("%d ", arr[i]);
        }

        arr2(arr, n);

        for(int i = 0; i < n; i++){
        
            System.out.printf("%d ", arr[i]);
        }

    



        
    }

    public static void arr2(int[] arr, int n){
        
        for(int i = 0; i < n; i++){
            if(arr[i] % 2 == 0){
                arr[i] /= 2;

            }
        }

        
    }
}