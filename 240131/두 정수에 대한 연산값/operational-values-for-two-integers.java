import java.util.Scanner;

public class Main {
    public static void asmor(int x ,int y){
        System.out.printf("%d %d", x*2, y+25);

    }

    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        

        if(a < b){
            asmor(a, b);
        }
        else {
            asmor(b, a);
        }
        // 여기에 코드를 작성해주세요.
    }
}