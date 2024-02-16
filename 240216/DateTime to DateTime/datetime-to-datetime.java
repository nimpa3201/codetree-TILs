import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);
        int day1 = 11;
        int hour1 = 11;
        int mins1 = 11;

        int day2 = sc.nextInt();
        int hour2 = sc.nextInt();
        int mins2 = sc.nextInt();
        int c = 0;

        
        while(true) {
            if(day1 == day2 && hour1 == hour2 && mins1 == mins2){
                break;
            }
            
            mins1++;
            c++;

        
            if(mins1 == 60) {
                hour1++;
                mins1 = 0;

            }
            if(hour1 == 24){
                day1++;
                hour1 = 0;

            }

        }
        
        System.out.println(c);
    }
}