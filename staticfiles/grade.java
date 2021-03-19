import java.util.*;
public class grade {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int mylist[][] = new int [6][6];
        int add[] = new int [16];
        System.out.println("enter the 6x6 matrix");
        for (int i = 0 ; i < 6; i++){
            for(int j = 0 ; j < 6; j++){
                System.out.println("enter the "+i+"x"+j+" :");
                mylist[i][j] = s.nextInt();
            }
        }
        for (int i = 0 ; i < 6; i++){
            System.out.println();
            for(int j = 0 ; j < 6; j++){
                System.out.print(mylist[i][j] + "   ");
            }
        }
        int k =0;
        for (int i = 0 ; i < 6; i++){
            for(int j = 0 ; j < 6; j++){
                if(i <= 3)
                if(j <= 3){
                    add[k]= mylist[i][j] + mylist[i][j+1] + mylist[i][j+2]+mylist[i+1][j+1] +mylist[i+2][j] + mylist[i+2][j+1] + mylist[i+2][j+2];
                    k++;
                }    
        }
    }
        for(int  i =0 ; i < add.length;i++){
            System.out.println();
            System.out.println(add[i]);
        }
        int max = add[0];
        for(int  i =0 ; i < add.length;i++){
            if (add[i] > max){
                max=add[i];
            }
        }
        System.out.println("maximum sum :"+ max);
}
}
