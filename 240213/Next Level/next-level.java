import java.util.Scanner;

class data_1{
    String di;
    int level;


    data_1(){
        di = "codetree";
        level = 10;

    }

    data_1(String x, int y){
        di = x;
        level = y;
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        String a = sc.next();
        int b = sc.nextInt();

        data_1 user1 = new data_1();

        data_1 user2 = new data_1(a, b);



        
        System.out.printf("user %s lv %d\n", user1.di, user1.level);
        System.out.printf("user %s lv %d\n", user2.di, user2.level);




        // 여기에 코드를 작성해주세요.
    }
}