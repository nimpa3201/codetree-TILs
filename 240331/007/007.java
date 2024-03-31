class student {
    int k, e, m;

    public student(){
        
    }

    public student(int q, int w, int e){
        this.k = q;
        this.e = w;
        this.m = e;
    }
}
public class Main{
    public static void main(String[] args){
        student student1 = new student();

        System.out.printf("%d %d %d", student1.k, student1.e, student1.m);

        
    } 
}