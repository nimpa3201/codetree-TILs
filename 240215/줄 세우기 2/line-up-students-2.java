import java.util.Scanner;
import java.util.Arrays;

class student implements Comparable<student>{

    int hi;
    int gr;
    int number;

    student(){}

    student(int hi, int gr, int number){
        this.hi = hi;
        this.gr = gr;
        this.number = number;

    } 

    public int compareTo(student students){
        if(this.hi == students.hi){
            return students.gr - this.gr;

        }
        return this.hi - students.hi;

    }
}
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        student[] students = new student[n];


        for(int i = 0; i < n; i++){

            int hi = sc.nextInt();
            int gr = sc.nextInt();
            int number = i+1;

            students[i] = new student(hi, gr, number);

        }


        Arrays.sort(students);

        


        for(int i = 0; i < n; i++){
            System.out.printf("%d %d %d\n", students[i].hi, students[i].gr, students[i].number);
        }

        
        // 여기에 코드를 작성해주세요.
    }
}