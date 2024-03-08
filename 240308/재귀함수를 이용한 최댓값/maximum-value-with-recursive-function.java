import java.util.Scanner;

public class Main {
    static int[] arr;


    public static int arr2(int n){

        if(n == 0){
            
            return arr[n];

        }

        return Math.max(arr2(n -1),arr[n]);
    
          
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        arr = new int[n];


        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();

        }
        System.out.printf("%d", arr2(n-1));

        // 여기에 코드를 작성해주세요.
    }
}