import java.io.*;
import java.util.*;
 
 
class test {
    static boolean DEBUG_FLAG = false;
    int INF = (int)1e9;
    long MOD = 1000000007;
    
    static void debug(String s) {
        if(DEBUG_FLAG) {
            System.out.print(s);
        }
    }
    
    int[] a, mod;
    long[] med;
    
    void bmed(int idx, int s, int e) {
        if(s==e) {
            med[idx] = a[s];
            return;
        }
        int left = 2*idx, right = left+1, m = (s+e)/2;
        bmed(left, s, m);
        bmed(right, m+1, e);
        med[idx] = med[left] + med[right];
    }
    
    void bmod(int idx, int s, int e) {
        if(s==e) {
            mod[idx] = s;
            return;
        }
        int left = 2*idx, right = left+1, m = (s+e)/2;
        bmod(left, s, m);
        bmod(right, m+1, e);
        mod[idx] = a[mod[left]]>a[mod[right]]?mod[left]:mod[right];
    }
    
    int getmod(int idx, int s, int e, int l, int r) {
        if(r<s || e<l) {
            return 0;
        }
        if(l<=s && e<=r) {
            return mod[idx];
        }
        int left = 2*idx, right = left+1, m = (s+e)/2;
        int x = getmod(left, s, m, l, r);
        int y = getmod(right, m+1, e, l, r);
        return a[x]>a[y]?x:y;
    }
    
    int getmed(int idx, int s, int e, long p) {
        if(s==e) {
            return s;
        }
        int left = 2*idx, right = left+1, m = (s+e)/2;
        if(p<=med[left]) {
            return getmed(left, s, m, p);
        }
        return getmed(right, m+1, e, p-med[left]);
    }
    
    void updmod(int idx, int s, int e, int p, int v) {
        if(s==e) {
            a[s] = v;
            return;
        }
        int left = 2*idx, right = left+1, m = (s+e)/2;
        if(p<=m) updmod(left, s, m, p, v);
        else updmod(right, m+1, e, p, v);
        mod[idx] = a[mod[left]]>a[mod[right]]?mod[left]:mod[right];
    }
    
    void updmed(int idx, int s, int e, int p, int v) {
        if(s==e) {
            med[idx] = v;
            return;
        }
        int left = 2*idx, right = left+1, m = (s+e)/2;
        if(p<=m) updmed(left, s, m, p, v);
        else updmed(right, m+1, e, p, v);
        med[idx] = med[left] + med[right];
    }
    
    long getsum(int idx, int s, int e, int l, int r) {
        if(r<s || e<l) return 0;
        if(l<=s && e<=r) return med[idx];
        int left = 2*idx, right = left+1, m = (s+e)/2;
        long x = getsum(left, s, m, l, r);
        long y = getsum(right, m+1, e, l, r);
        return x + y;
    }
    
    long gcd(long a, long b) {
        if(b==0) return a;
        return gcd(b, a%b);
    }
    
    void solve(InputReader in, PrintWriter out) throws IOException {
        int n = in.nextInt();
        int q = in.nextInt();
        a = new int[n+1];
        for(int i=1; i<=n; i++) {
            a[i] = in.nextInt();
        }
        int sz = (int)Math.pow(2, Math.ceil(Math.log(n)/Math.log(2)));
        mod = new int[2*sz];
        med = new long[2*sz];
        bmod(1, 1, n);
        bmed(1, 1, n);
        while(q-->0) {
            int tp = in.nextInt();
            if(tp==1) {
                int l = in.nextInt();
                int r = in.nextInt();
                long s1 = getsum(1, 1, n, l, r);
                long s2 = 0;
                if(l>1) {
                    s2 = getsum(1, 1, n, 0, l-1);
                }
                int mode = getmod(1, 1, n, l, r);
                int median = 0;
                if(s1%2==0) {
                    int m1 = getmed(1, 1, n, s2+s1/2);
                    int m2 = getmed(1, 1, n, s2+s1/2+1);
                    median = (m1+m2)/2;
                } else {
                    median = getmed(1, 1, n, s2+s1/2+1);
                }
                long rs = gcd(mode, median);
                rs = (mode*(median*1l))/rs;
                out.println(rs);
            } else {
                int p = in.nextInt();
                int v = in.nextInt();
                updmod(1, 1, n, p, v);
                updmed(1, 1, n, p, v);
            }
        }
    }
    
    
    public static void main(String[] args) throws IOException {
        if(args.length>0 && args[0].equalsIgnoreCase("d")) {
            DEBUG_FLAG = true;
        }
        InputReader in = new InputReader();
        PrintWriter out = new PrintWriter(System.out);
        int t = in.nextInt();
        long start = System.nanoTime();
        while(t-- >0) {
            new test().solve(in, out);
        }
        long end = System.nanoTime();
        debug("\nTime: " + (end-start)/1e6 + " \n\n");
        out.close();
    }
    
    static class InputReader {
        static BufferedReader br;
        static StringTokenizer st;
    
        public InputReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        
        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        int nextInt() {
            return Integer.parseInt(next());
        }
        
        long nextLong() {
            return Long.parseLong(next());
        }
        
        double nextDouble() {
            return Double.parseDouble(next());
        }
    }
} 