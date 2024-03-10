import java.util.Scanner;


class data_1{

    String id;
    int level;

    public data_1(){
        this.id = "codetree";
        this.level = 10;

        
    }

    public data_1(String a, int b){
        this.id = a;
        this.level = b;

    }


    
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        String a = sc.next();
        int b = sc.nextInt();

        data_1 user1 = new data_1();

        data_1 user2 = new data_1(a, b);



        
        System.out.printf("user %s lv %d\n", user1.id, user1.level);
        System.out.printf("user %s lv %d\n", user2.id, user2.level);




        // 여기에 코드를 작성해주세요.
    }
}