import java.util.Scanner;

class space{
    String code;
    char local;
    int time;

    public space(String q, char w, int e){
        this.code = q;
        this.local = w;
        this.time = e;

    }


}

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        String a = sc.next();
        char b = sc.next().charAt(0);
        int c = sc.nextInt();

        space a1 = new space(a, b, c);

        System.out.printf("secret code : %s\n", a1.code);
        System.out.printf("meeting point : %c\n", a1.local);
        System.out.printf("time : %d\n", a1.time);


        
        // 여기에 코드를 작성해주세요.
    }
}