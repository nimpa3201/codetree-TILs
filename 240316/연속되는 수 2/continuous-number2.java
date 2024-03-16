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
        int c2 = 0;


        for(int i = 0; i < n; i++){
            if( i == 0 || arr[i] == arr[i -1]){
                c++;
            }
            else{
                if(c2 < c){
                    c2 = c;
                    
                }
                c = 0;

            }
        }
        c2++;

        System.out.printf("%d", c2);


        // 여기에 코드를 작성해주세요.
    }
}