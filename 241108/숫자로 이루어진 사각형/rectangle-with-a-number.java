import java.util.Scanner;

public class Main {

    public static void printNum(int n){
        int cnt = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cnt++;
                System.out.printf("%d ", cnt);
                if(cnt == 9){
                    cnt = 0;
                }
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        printNum(n);


        // 여기에 코드를 작성해주세요.
    }
}