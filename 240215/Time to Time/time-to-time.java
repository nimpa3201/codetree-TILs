import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);
        
        int hour = sc.nextInt();
        int mins = sc.nextInt();

        int elapsedTime = 0;

        int hour2 = sc.nextInt();
        int mins2 = sc.nextInt();


        while(true) {
            if(hour == hour2 && mins == mins2)
                break;
            

            elapsedTime++;
            mins++;

            if(mins == 60) {
                hour++;
                mins = 0;
            }
        }
        
        System.out.print(elapsedTime);
    }
}