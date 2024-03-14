import java.util.Scanner;

class superr{
    String name;
    int code;

    public superr(){
        this.name = "codetree";
        this.code = 50;

    }

    public superr(String name,int code){
        this.name = name;
        this.code = code;
    }

};

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        String name = sc.next();
        int code = sc.nextInt();

        superr spuerr1 = new superr();
        superr spuerr2 = new superr(name, code);

        System.out.printf("product %d is %s\n", spuerr1.code, spuerr1.name);
        System.out.printf("product %d is %s\n", spuerr2.code, spuerr2.name);
        // 여기에 코드를 작성해주세요.
    }
}