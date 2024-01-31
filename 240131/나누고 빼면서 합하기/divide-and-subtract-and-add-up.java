import java.util.Scanner;

public class Main {
    public static int s = 0;



    public static int arr2(int a, int[] arr){
        
        s += arr[a-1];

        while(a != 1){

            

            if(a % 2 == 1){
                a--;

            }
            else{
                a /= 2;

            }

            s += arr[a-1];

        }
        return s;

    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        int m = sc.nextInt();


        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
            
        }

        System.out.printf("%d",arr2(m, arr));

        // 여기에 코드를 작성해주세요.
    }
}