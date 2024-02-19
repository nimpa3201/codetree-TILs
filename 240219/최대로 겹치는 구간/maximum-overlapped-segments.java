import java.util.Scanner;


public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        int[] arr = new int[n*2];

        for(int i = 0; i < n; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();

            arr[i*2] = a;
            arr[i*2 + 1] = b;

        }
        int box = 0;


        for(int i = 0; i < n*2; i++){
            if(arr[i] < box){
                box = arr[i];

            }
        }
        box *= -1;

        
        for(int i = 0; i < n*2; i++){
            arr[i] += box;
        }

        int max = arr[0];

        for(int i = 0; i < n*2; i++){

            if(arr[i] > max){
                max = arr[i];

            }


        }

        int[] arr2 = new int[max];


        for(int i = 0; i < n; i++){
            for(int j = arr[i*2]; j < arr[i*2+1]; j++){
                arr2[j]++;

            }
        }

        int c = 0;

        for(int i = 0; i < max; i++){
            //System.out.printf("%d ", arr2[i]);
            if(c < arr2[i]){
                c = arr2[i];

            }
        }

        System.out.printf("%d ", c);






        


        // 여기에 코드를 작성해주세요.
    }
}