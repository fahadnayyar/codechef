import java.io.*;
import java.util.*;
 
//I am fading.......
//read the question correctly (is y a vowel? what are the exact constraints?)
//look out for SPECIAL CASES (n=1?) and overflow (ll vs int?)
public class Main1
{
	static class segtree
	{
	//segment tree
	
	//n is segment tree size
	//take input from i=n to 2*n-1
	int n;
	pair[]tr;
	combiner co;
	void build(long []a)
	{
		n=a.length;
		tr=new pair[2*n];
		for(int i=0; i<n; i++)
			tr[n+i]=new pair(a[i],i+1);
		for(int i=n-1; i>0; i--)
			tr[i]=co.combine(tr[i<<1],tr[(i<<1)|1]);
	}
	void modify(int p, int value)
	{
		
		for(tr[p+=n]=new pair(value,p+1-n); p>1; p>>=1)
			tr[p>>1]=co.combine(tr[p],tr[p^1]);
	}
	pair query(int l, int r)
	{
//		r++;
		//both are inclusive
		pair res=new pair(0,0);
		for(l+=n, r+=n; l<r; l>>=1,r>>=1)
		{
			if(l%2!=0) res=co.combine(res,tr[l++]);
			if(r%2!=0) res=co.combine(res,tr[--r]);
		}
		return res;
	}
	}
	public static void main(String[] args) throws Exception
	{
		int t=ni();
		while(t-->0)
		{
			int n=ni(),q=ni();
			long[]a=nla(n);
			segtree mode=new segtree();
			mode.co=new combiner()
					{
				public pair combine(pair a,pair b)
				{
					if(a.a>b.a)
						return a;
					else return b;
				}
					};
			mode.build(a);
			ssegtree sum=new ssegtree();
			sum.build(a);
			while(q-->0)
			{
				if(ni()==1)
				{
					int l=ni(),r=ni();
					long mod=mode.query(l-1, r).b;
					long su=sum.query(l-1, r);
					int low=l-1,high=r,mid=(low+high)/2;
					while(low<high)
					{
						if(sum.query(l-1, mid)*2>su)
							high=mid;
						else
							low=mid+1;
						mid=(low+high)/2;
					}
					if(mid!=0)
					if(sum.query(l-1, mid-1)*2==su)
						mid--;
					sop((mod*(mid+0L))/gcd(mod+0L,mid+0L));
				}
				else
				{
					int ind=ni(),val=ni();
					mode.modify(ind-1, val);
					sum.modify(ind-1, val);
				}
			}
		}
		System.out.print(output);
	}
	static class ssegtree
	{
	//segment tree
	
	//n is segment tree size
	//take input from i=n to 2*n-1
	int n;
	long[]tr;
//	combiner co;
	void build(long[]a)
	{
		n=a.length;
		tr=new long[2*n];
		System.arraycopy(a, 0, tr, n, n);
		for(int i=n-1; i>0; i--)
			tr[i]=tr[i<<1]+tr[(i<<1)|1];
	}
	void modify(int p, int value)
	{
		for(tr[p+=n]=value; p>1; p>>=1)
			tr[p>>1]=tr[p]+tr[p^1];
	}
	long query(int l, int r)
	{
//		r++;
		//both are inclusive
		long res=0;
		for(l+=n, r+=n; l<r; l>>=1,r>>=1)
		{
			if(l%2!=0) res=res+tr[l++];
			if(r%2!=0) res=res+tr[--r];
		}
		return res;
	}
	}
	///////////////////////////////////////////
	///////////////////////////////////////////
	///template from here
	
	static class pair
	{
		long a;
		int b;
		pair(){}
		pair(long c,int d){a=c;b=d;}
	}
	static interface combiner
	{
		
		public pair combine(pair a, pair b);
	}
	static final int mod=1000000007;
	static final double eps=1e-9;
	static final long inf=100000000000000000L;
	static Reader in=new Reader();
	static StringBuilder output=new StringBuilder();
	static Random rn=new Random();
	static void reverse(int[]a){for(int i=0; i<a.length/2; i++){a[i]^=a[a.length-i-1];a[a.length-i-1]^=a[i];a[i]^=a[a.length-i-1];}}
	static void sort(int[]a)
	{
		int te;
		for(int i=0; i<a.length; i+=2)
		{
			te=rn.nextInt(a.length);
			if(i!=te)
			{
				a[i]^=a[te];
				a[te]^=a[i];
				a[i]^=a[te];
			}
		}
		Arrays.sort(a);
	}
	static void sort(long[]a)
	{
		int te;
		for(int i=0; i<a.length; i+=2)
		{
			te=rn.nextInt(a.length);
			if(i!=te)
			{
			a[i]^=a[te];
			a[te]^=a[i];
			a[i]^=a[te];
			}
		}
		Arrays.sort(a);
	}
	static void sort(double[]a)
	{
		int te;
		double te1;
		for(int i=0; i<a.length; i+=2)
		{
			te=rn.nextInt(a.length);
			if(i!=te)
			{
			te1=a[te];
			a[te]=a[i];
			a[i]=te1;
			}
		}
		Arrays.sort(a);
	}
	static void sort(int[][]a)
	{
		Arrays.sort(a, new Comparator<int[]>()
		{
			public int compare(int[]a,int[]b)
			{
				if(a[0]>b[0])
					return -1;
				if(b[0]>a[0])
					return 1;
				return 0;
			}
		});
	}
	static void sort(pair[]a)
	{
		Arrays.sort(a,new Comparator<pair>()
				{
			@Override
			public int compare(pair a,pair b)
			{
				if(a.a>b.a)
					return 1;
				if(b.a>a.a)
				return -1;
				return 0;
			}
				});
	}
	static int log2n(long a)
	{
		int te=0;
		while(a>0)
		{
			a>>=1;
			++te;
		}
		return te;
	}
	@SuppressWarnings("rawtypes")
	static class vecti implements Iterable
	{
		int a[],size;
		vecti(){a=new int[10];size=0;}
		vecti(int n){a=new int[n];size=0;}
		public void add(int b){if(++size==a.length)a=Arrays.copyOf(a, 2*size);a[size-1]=b;}
		public void sort(){Arrays.sort(a, 0, size);}
		public void sort(int l, int r){Arrays.sort(a, l, r);}
		@Override
		public ListIterator<Integer> iterator() {
			ListIterator hola=new ListIterator()
					{
				int cur=0;
						@Override
						public boolean hasNext() {
							return cur<size;
						}
 
						@Override
						public Object next() {
							return a[cur++];
						}
 
						@Override
						public boolean hasPrevious() {
							return cur>0;
						}
 
						@Override
						public Object previous() {
							return a[--cur];
						}
 
						@Override
						public int nextIndex() {
							// TODO Auto-generated method stub
							return 0;
						}
 
						@Override
						public int previousIndex() {
							// TODO Auto-generated method stub
							return 0;
						}
 
						@Override
						public void remove() {
							// TODO Auto-generated method stub
							
						}
 
						@Override
						public void set(Object e) {
							// TODO Auto-generated method stub
							
						}
 
						@Override
						public void add(Object e) {
							// TODO Auto-generated method stub
							
						}
				
					};
			return hola;
		}
	}
	//output functions////////////////
	static void pr(Object a){output.append(a+"\n");}
	static void pr(){output.append("\n");}
	static void p(Object a){output.append(a);}
	static void pra(int[]a){for(int i:a)output.append(i+" ");output.append("\n");}
	static void pra(long[]a){for(long i:a)output.append(i+" ");output.append("\n");}
	static void pra(String[]a){for(String i:a)output.append(i+" ");output.append("\n");}
	static void pra(double[]a){for(double i:a)output.append(i+" ");output.append("\n");}
	static void sop(Object a){System.out.println(a);}
	static void flush(){System.out.println(output);output=new StringBuilder();}
	//////////////////////////////////
	//input functions/////////////////
	static int ni(){return Integer.parseInt(in.next());}
	static long nl(){return Long.parseLong(in.next());}
	static String ns(){return in.next();}
	static double nd(){return Double.parseDouble(in.next());}
	static int[] nia(int n){int a[]=new int[n];for(int i=0; i<n; i++)a[i]=ni();return a;}
	static int[] pnia(int n){int a[]=new int[n+1];for(int i=1; i<=n; i++)a[i]=ni();return a;}
	static long[] nla(int n){long a[]=new long[n];for(int i=0; i<n; i++)a[i]=nl();return a;}
	static String[] nsa(int n){String a[]=new String[n];for(int i=0; i<n; i++)a[i]=ns();return a;}
	static double[] nda(int n){double a[]=new double[n];for(int i=0; i<n; i++)a[i]=nd();return a;}
	//////////////////////////////////
	//some utility functions
	static void exit(){System.out.print(output);System.exit(0);}
	static int min(int... a){int min=a[0];for(int i:a)min=Math.min(min, i);return min;}
	static int max(int... a){int max=a[0];for(int i:a)max=Math.max(max, i);return max;}	
	static int gcd(int... a){int gcd=a[0];for(int i:a)gcd=gcd(gcd, i);return gcd;}	
	static long min(long... a){long min=a[0];for(long i:a)min=Math.min(min, i);return min;}
	static long max(long... a){long max=a[0];for(long i:a)max=Math.max(max, i);return max;}	
	static long gcd(long... a){long gcd=a[0];for(long i:a)gcd=gcd(gcd, i);return gcd;}	
	static String pr(String a, long b){String c="";while(b>0){if(b%2==1)c=c.concat(a);a=a.concat(a);b>>=1;}return c;}
	static long powm(long a, long b, long m){long an=1;long c=a;while(b>0){if(b%2==1)an=(an*c)%m;c=(c*c)%m;b>>=1;}return an;}
	static int gcd(int a, int b){if(b==0)return a;return gcd(b, a%b);}
	static long gcd(long a, long b){if(b==0)return a;return gcd(b, a%b);}
	static class Reader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;
        public Reader() {
            reader = new BufferedReader(new InputStreamReader(System.in), 32768);
            tokenizer = null;
        }
        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
    }
} 