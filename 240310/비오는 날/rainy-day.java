import java.util.Scanner;


    class data{
        String day;
        String week;
        String weather;

        public data(){
            this.day = "";
            this.week = "";
            this.weather = "";

        }

        public data(String day, String week, String weather){
            this.day = day;
            this.week = week;
            this.weather = weather;
        }

    };


public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        data[] datas = new data[n];

        for(int i = 0; i < n; i++){
            String day = sc.next();
            String week = sc.next();
            String weather = sc.next();
            
            datas[i] = new data(day, week, weather);
        }
        //System.out.printf("%s %s %s\n", datas[1].day, datas[1].week, datas[1].weather);
        String cc = "Rain";

        for(int i = 0; i < n; i++){
            System.out.printf("%s %s %s\n", datas[i].day, datas[i].week, datas[i].weather);
            
            if(datas[i].weather.equals(cc)){
                System.out.printf("%d\n",1);
            }
            
        }
        
        // 여기에 코드를 작성해주세요.
    }
}