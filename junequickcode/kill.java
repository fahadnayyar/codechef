import java.io.*;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.*;
 
 
 
 
class Krillin {
  static void print(Object...x){
    for(Object y : x)
      if(y instanceof boolean[]){
        System.out.print(Arrays.toString((boolean[])y)+",");
      }
      else if(y instanceof long[]){
        System.out.print(Arrays.toString((long[])y)+",");
      }
      else if(y instanceof int[][]){
        System.out.println();
        for(int[] z : (int[][])y){
          System.out.println(Arrays.toString(z));
        }
      }else if(y instanceof int[]){
        System.out.print(Arrays.toString((int[])y)+",");
      }
      else if(y instanceof long[][]){
        System.out.println();
        for(long[] z : (long[][])y){
          System.out.println(Arrays.toString(z));
        }
      }else if(y instanceof long[]){
        System.out.print(Arrays.toString((int[])y)+",");
      }else{
        System.out.print(y + ",");
      }
    System.out.println();
  }
 
 
 
  static class Stopwatch{
    static NumberFormat FORMAT = new DecimalFormat("0.000");
 
    long t0;
    Stopwatch(){
      start();
    }
   
    void start(){
      t0 = System.currentTimeMillis();      
    }
    
    long elapsed(){
      return System.currentTimeMillis()-t0;
    }
    
    void printElapsed(){
      long x = elapsed();
      System.out.println("Time: " + FORMAT.format(x*0.001));
    }
    
  }
 
 
 
 
 
 
 
 
 
  static boolean isDigit(char c){
    return c >= '0' && c <= '9';
  }
 
  static int getDigit(char c){
    return c - '0';
  }
 
  public static int nextInt(Reader r){
    int ret = 0;
    boolean neg = false;
    try{
      while(true){
        char c = (char) r.read();
        if(c == '-'){
          neg = true;
          continue;
        }
        if(isDigit(c)){
          ret = getDigit(c);
          break;
        }
      }
      while(true){
        char c = (char) r.read();
        if(isDigit(c)){
          ret = 10*ret + getDigit(c);
        }else{
          break;
        }
 
      }
    }catch(Exception e){}
    if(neg)
      ret = -ret;
    return ret;
 
  }
 
  public static long nextLong(Reader r){
    long ret = 0;
    boolean neg = false;
 
    try{
      while(true){
        char c = (char) r.read();
        if(c == '-'){
          neg = true;
          continue;
        }
 
        if(isDigit(c)){
          ret = getDigit(c);
          break;
        }
      }
      while(true){
        char c = (char) r.read();
        if(isDigit(c)){
          ret = 10*ret + getDigit(c);
        }else{
          break;
        }
 
      }
    }catch(Exception e){}
    if(neg)
      ret = -ret;
 
    return ret;
 
  }
 
 
  public static double nextDouble(Reader r){
    double ret = 0;
    boolean neg = false;
 
    try{
      while(true){
        char c = (char) r.read();
        if(c == '-'){
          neg = true;
          continue;
        }
 
        if(isDigit(c)){
          ret = getDigit(c);
          break;
        }
      }
      while(true){
        char c = (char) r.read();
        if(isDigit(c)){
          ret = 10*ret + getDigit(c);
        }else{
          break;
        }
 
      }
 
      double q = 0.1;
      while(true){
        char c = (char) r.read();
        if(isDigit(c)){
          ret = ret + getDigit(c)*q;
          q /= 10;
        }else{
          break;
        }
 
      }
 
    }catch(Exception e){}
    if(neg)
      ret = -ret;
 
    return ret;
 
  }
 
  public static String nextString(Reader r){
    StringBuilder sb = new StringBuilder();
    sb.append(skipWhite(r));
    try{
      while(true){
        char c = (char) r.read();
        if(Character.isWhitespace(c))
          break;
        sb.append(c);
      }
 
    }catch(Exception e){}
    return sb.toString();
 
  }
  static int[] nextInts(Reader r, int n){
    int[] ret = new int[n];
    for(int i=0; i<n; ++i)
      ret[i] = nextInt(r);
    return ret;
  }
 
  public static char skipWhite(Reader r){
    try{
      while(true){
        char c = (char) r.read();
        if(!Character.isWhitespace(c))
          return c;          
      }
    }catch(Exception e){}
    return ' ';
  }
 
 
  static void goFile(String s) throws Exception{
    go(new FileReader(new File(s)));
  }
 
  static void go() throws NumberFormatException, Exception{
    go(new InputStreamReader(System.in));
  }
 
  
  
  
  
  
  
  static void go(Reader r) throws Exception{
    int t = nextInt(r);
    for(int i=0; i<t; ++i){
      int n = nextInt(r);  
      int q = nextInt(r);      
      long[] A = new long[n];
      for(int j=0; j<n; ++j){
        A[j] = nextInt(r);
      }
      int[] Q = new int[q*3];
      for(int j=0; j<q*3; ++j){
        Q[j] = nextInt(r);
      }
      solve(A,Q);
    }
  }
 
 
  static class MaxArray {
 
    private final long[][] arrs;
 
    private static int roundUp(int n){
      int ret = 1;
      int nn = n;
      while(n != 0){
        ret <<= 1;
        n >>= 1;
      }
      if(ret == nn*2)
        ret >>= 1;
      return ret;
    }
    
    public MaxArray(int n) {
      if(n <= 1)
        n=2;
 
      n = roundUp(n)-1;
      List<long[]> larrs = new ArrayList<>();
      while(n > 0){
        larrs.add(new long[n+1]);
        n >>= 1;
      }
      arrs = larrs.toArray(new long[0][]);
    }
 
    public MaxArray(long[] x) {
      this(x.length);
      for(int i=0; i<x.length; ++i)
        arrs[0][i] = x[i];
      for(int i = x.length; i<arrs[0].length; ++i)
        arrs[0][i] = Long.MIN_VALUE;
      
      for(int i=1; i<arrs.length; ++i){
        long[] z = arrs[i];
        long[] z0 = arrs[i-1];
        for(int j=0; j<z.length; ++j)
          z[j]=Math.max(z0[j*2], z0[j*2+1]);
      }
      
    }
 
 
    public void setValue(int k, long x){
      arrs[0][k] = x;
      for(int i=1; i<arrs.length; ++i){
        k/=2;
        arrs[i][k] = Math.max(arrs[i-1][k*2], arrs[i-1][k*2+1]);
      }
    }
 
    
    public long getValue(int k){
      return arrs[0][k];
    }
    
    // max of values in [a,b)
    public long getMax(int a, int b){
      b -= 1;
      long ret = Long.MIN_VALUE;
      for(long[] z : arrs){
        if(b<a)
          break;
        if(a == b){
          ret = Math.max(ret, z[a]);
          break;
        }
        if((a&1) == 1){
          ret = Math.max(ret, z[a]);
          a += 1;
        }
        if((b&1) == 0){
          ret = Math.max(ret, z[b]);
          b -= 1;
        }
        a /= 2;
        b /= 2;
      }
      return ret;
 
    }
    
    public int whichMax(int a, int b){
      long mx = getMax(a,b);
      while(b>a+1){
        int c = (a+b)/2;
        if(getMax(a,c)==mx)
          b=c;
        else
          a=c;
      }
      return a;
    }
    
    static long max(long[] x, int a, int b){
      long ret = Long.MIN_VALUE;
      for(int i = a; i<b; ++i)
        ret = Math.max(ret, x[i]);
      return ret;
    }
    
    
  }
 
  static class CumulArray {
 
    private final long[][] arrs;
 
    public CumulArray(int n) {
      List<long[]> larrs = new ArrayList<>();
      while(n > 0){
        larrs.add(new long[n+1]);
        n >>= 1;
      }
      arrs = larrs.toArray(new long[0][]);
    }
 
    public long getValue(int k){
      return arrs[0][k];
    }
 
    public void setValue(int k, long x){
      insert(k,x- arrs[0][k]);
    }
 
    public void insert(int k, long delta){
      for(long[] z : arrs){
        z[k] += delta;
        k >>= 1;
      }    
    }
    
    // sum of values in [0,k)
    public long getCount(int k){
      long ret = 0;
      for(long[] z : arrs){
        if((k&1) != 0)
          ret += z[k-1];
        k >>= 1;
      }
      return ret;
 
    }
    
    public long getCount(int a, int b){
      return getCount(b)-getCount(a);
    }
 
    public int getMedian(int a, int b){
      long tot = getCount(a,b);
      int b0 = b;
      while(b>a+1){
        int c = (a+b)/2;
        long top = getCount(c,b0);
        long bot = tot-top;
        if(top > bot)
          a = c;
        else
          b = c;
          
      }
      return a;
    }
    
 
    
  }
 
  public static long gcd(long a, long b){
    while( b!= 0){
      long temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }
 
  public static long lcm(long a, long b){
    return (a/gcd(a,b))*b;
  }
  
 
  private static void solve(long[] A, int[] Q) {
    int n = A.length;
    MaxArray max = new MaxArray(A);
    CumulArray cum = new CumulArray(A.length);
    for(int i=0; i<n; ++i)
      cum.setValue(i, A[i]);
    
    for(int i=0; i<Q.length; i+=3){
      int t = Q[i];
      if(t == 1){
        int L = Q[i+1]-1;
        int R = Q[i+2];
        int mode = max.whichMax(L, R)+1;
        int med = cum.getMedian(L, R)+1;
        System.out.println(lcm(mode,med));
      }else{
        int I = Q[i+1]-1;
        int a = Q[i+2];
        max.setValue(I, a);
        cum.setValue(I, a);
      }
    }
  }
 
  public static void main(String[] args) throws Exception{
    go();
//    goFile("input/temp.txt");
  }
 
}
 