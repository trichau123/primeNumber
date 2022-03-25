class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        int a = IsItPrime(13);
        if(a == 1){
           System.out.println("Prime");
        }else{
            System.out.println("NOT Prime");}
    }
 
  public static int IsItPrime(int number) {
   int i;
   int aux,count;
   count = 1;
   aux = number;
   for (i = 1; i < number; i++) {
         aux = number % i;  
        System.out.println(aux);
        if (aux == 0){
          count ++;
          System.out.println(count);
          }      
   }
    if (count == 2)//no remainder not
      return 1;
    return 0;
  }
}
