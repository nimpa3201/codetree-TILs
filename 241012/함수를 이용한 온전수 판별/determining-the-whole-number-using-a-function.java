import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int cnt = 0;
        for(int i=n; i<=m; i++) {
            if(isOnjeonsu(i)) {
                cnt ++;
            }
        }

        System.out.print(cnt);

    }

    public static boolean isOnjeonsu(int i) {
        if((i%2 != 0 && i%10 != 5) && (i%3 != 0 || i %9 ==0)){ 
            return true;
        } 
         return false;
    }
}