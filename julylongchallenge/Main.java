//package codechef;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
class Main {
	public static void main(String[] args) throws IOException{
		Reader.init(System.in);
		int t = Reader.nextInt();
		for (int w=0;w<t;w++) {
			int n =Reader.nextInt();
			int k =Reader.nextInt();
			int arr[] = new int[n];
			for (int i=0;i<n;i++) {
				arr[i]=Reader.nextInt();
			}
			Arrays.sort(arr);
			int p = 1000000007;
			int p1 = 1000000006;
			int ncrar[][] = giveNcr(n, p1);
			//System.out.println(ncrar[n][2]);
			int kyadalo = ncrar[n-1][k-1];
			int expoar[] = new int[n];
			for (int i=0;i<n;i++) {
				expoar[i]=kyadalo;
			}
			for (int i=0;i<=n-k;i++) {
				int kyakamkare = ncrar[n-i-1][k-1];
				expoar[i] = (expoar[i]%p1 - kyakamkare%p1) %p1;
			}
			for (int i=k-1;i<n;i++) {
				int kyakamkare = ncrar[i][k-1];
				expoar[i] = (expoar[i]%p1 - kyakamkare%p1) %p1;
			}
			long ans=1;
			for (int i=1;i<n-1;i++) {
				long a = arr[i];
				long b = expoar[i];
				long y = b%p1;
				ans = ans%p;
				long kya =atobmodp(a, y, p)%p;
				long yo = (ans * kya);
				ans = yo%p;
			}
			System.out.println(ans);
			
		}
	}
	public static long atobmodp(long a, long y, long p) {
		long ret =1;
		a=a%p;
		while(y>0) {
			if ((y & 1) == 1) {
				long yo = ret*a;
				ret = yo %p;
			}
			y = y/2;
			long yo = a*a;
			a=yo%p;
			
			//a=(a*a)%p;
		}
		return ret;
	}
	public static int[][] giveNcr(int n , int p){
		int retar[][] = new int[n+1][n+1];
		for (int i =0 ; i<=n ;i ++) {
			for (int j=0;j<=n;j++) {
				if (i==j) {
					retar[i][j]=1;
				}else if (j==0) {
					retar[i][j]=1;
				}else if (i==0) {
					retar[i][j]=1;
				}
				else {
					retar[i][j] = (retar[i-1][j-1]%p + retar[i-1][j]%p)%p ; 
				}
			}
		}
	return retar;
	}
}




/** Class for buffered reading int and double values */
class Reader {
    static BufferedReader reader;
    static StringTokenizer tokenizer;

    /** call this method to initialize reader for InputStream */
    static void init(InputStream input) {
        reader = new BufferedReader(
                     new InputStreamReader(input) );
        tokenizer = new StringTokenizer("");
    }

    /** get next word */
    static String next() throws IOException {
        while ( ! tokenizer.hasMoreTokens() ) {
            //TODO add check for eof if necessary
            tokenizer = new StringTokenizer(
                   reader.readLine() );
        }
        return tokenizer.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt( next() );
    }
	
    static double nextDouble() throws IOException {
        return Double.parseDouble( next() );
    }
}