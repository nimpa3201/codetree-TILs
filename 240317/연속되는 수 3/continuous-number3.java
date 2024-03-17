import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();

        }
        int c = 0;
        int m = 0;
        int q = 0;

        for(int i = 0; i < n; i++){
            if(arr[i] < 0){
                c++;
                m = 0;
            }
            else{
                m++;
                c = 0;
            }
            q = Math.max(q,c);
            q = Math.max(q,m);


        }
        System.out.printf("%d", q);

        // 여기에 코드를 작성해주세요.
    }
}