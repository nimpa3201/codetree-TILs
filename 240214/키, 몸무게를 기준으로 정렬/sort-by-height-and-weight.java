import java.util.Scanner;
import java.util.Arrays;

class Student implements Comparable<Student> {
    String name;

    int tole;
    int grem;


    Student(){

    }
    Student(String name, int tole, int grem){
        this.name = name;
        this.tole = tole;
        this.grem = grem;
    }

    public int compareTo(Student students) {
        if(this.tole == students.tole){
            return students.grem - this.grem;
        }
        return this.tole - students.tole ;

    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        Student[] students = new Student[n];

        for(int i = 0; i < n; i++){
            String na = sc.next();
            int to = sc.nextInt();
            int gr = sc.nextInt();


            students[i] = new Student(na, to, gr);

        }

        
        Arrays.sort(students);

        for(int i = 0; i < n; i++){
            System.out.printf("%s %d %d\n", students[i].name, students[i].tole, students[i].grem);

        }



        // 여기에 코드를 작성해주세요.
    }
}