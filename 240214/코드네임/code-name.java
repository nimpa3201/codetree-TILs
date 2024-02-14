import java.util.Scanner;
 
class user{
    char name;
    int scor;

    user() {
        name = 0;
        scor = 0;

    }

    user(char name1, int scor1){
        name = name1;
        scor = scor1;

    }
        

};


public class Main {
   
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);
        
        user[] users = new user[5];

        for(int i = 0; i < 5; i++){
            char name = sc.next().charAt(0);
            int scor = sc.nextInt();

            users[i] = new user(name, scor);

        }
        char minname = users[0].name;

        int minco = users[0].scor;

        for(int i = 0; i < 5; i++){
            if(users[i].scor < minco){
                minco = users[i].scor;
                minname = users[i].name;
            }
        }

        System.out.printf("%c %d", minname, minco);



        // 여기에 코드를 작성해주세요.
    }
}