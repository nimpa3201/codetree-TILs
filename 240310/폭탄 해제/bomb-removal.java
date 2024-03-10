import java.util.Scanner;

class boo{
    String code;
    char color;
    int second;

    public boo() {
        this.code = "";
        this.color = ' ';
        this.second = 0;
    }

    public boo(String code, char color, int second) {
        this.code = code;
        this.color = color;
        this.second = second;    
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        String code = sc.next();

        char color = sc.next().charAt(0);

        int second = sc.nextInt();

        boo boo1 = new boo(code, color, second);

        System.out.printf("code : %s\n", boo1.code);
        System.out.printf("color : %c\n", boo1.color);
        System.out.printf("second : %d\n", boo1.second);
        
        // 여기에 코드를 작성해주세요.
    }
}