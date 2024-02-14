import java.util.Scanner;
import java.util.Arrays;

class Student implements Comparable<Student> {
    int tole;
    int grem;
    int c;

    Student(){

    }
    Student(int tole, int grem, int c){
        this.tole = tole;
        this.grem = grem;
        this.c = c;
    }

    public int compareTo(Student students) {
        if(this.tole == students.tole){
            if(this.grem == students.grem){
                return this.c - students.c;
            }
            return students.grem - this.grem;

        }
        return students.tole - this.tole;

    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        Student[] students = new Student[n];

        for(int i = 0; i < n; i++){
            int to = sc.nextInt();
            int gr = sc.nextInt();
            int c = i+1;


            students[i] = new Student(to, gr,c);

        }
        Arrays.sort(students);

        for(int i = 0; i < n; i++){
            System.out.printf("%d %d %d\n", students[i].tole, students[i].grem, students[i].c);

        }



        // 여기에 코드를 작성해주세요.
    }
}