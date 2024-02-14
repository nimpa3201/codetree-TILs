import java.util.Scanner;
 
class user{
    char name;
    int scor;

    public user() {
        this.name = 0;
        this.scor = 0;

    }

    public user(char name, int scor){
        this.name = name;
        this.scor = scor;

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
            if(minco > users[i].scor){
                minco = users[i].scor;
                minname = users[i].name;
            }
        }

        System.out.printf("%c %d", minname, minco);



        // 여기에 코드를 작성해주세요.
    }
}