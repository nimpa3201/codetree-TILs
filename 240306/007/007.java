import java.util.Scanner;

class value {
    String code;
    char place;
    int time;

    public value(String a, char b, int c){
        this.code = a;
        this.place = b;
        this.time = c;


    }
}





public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System. in);

        String a = sc.next();
        char b = sc.next().charAt(0);
        int c = sc.nextInt();

        value value2 = new value(a, b, c);

        System.out.printf("secret code : %s\n", value2.code);
        System.out.printf("meeting point : %c\n", value2.place);
        System.out.printf("time : %d\n", value2.time);




    }
}