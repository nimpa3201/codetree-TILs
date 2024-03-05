import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();

        }
        System.out.printf("%d",arr2(arr, m));


    }

    public static int arr2(int[] arr, int m){
        int s = 0;

        while(m > 1){

            s = arr[m];

            if(m % 2 == 0){
                m /= 2;

            }
            else{
                m -= 1;

            }
        } 
        return s;

    }
}