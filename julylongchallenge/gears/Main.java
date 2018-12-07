//16 50
//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
//2 1 2
//2 2 3
//2 3 4
//2 4 5
//2 5 1
//2 2 6
//2 6 7
//2 8 9
//2 10 11
//2 11 12
//2 12 13
//2 13 10
//2 12 14
//2 15 16


//package codechef;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Hashtable;
import java.util.Scanner;
import java.util.StringTokenizer;

class Main {
	public static void main(String[] args) throws IOException {
		Reader.init(System.in);
		int n = Reader.nextInt();
		int m = Reader.nextInt();
		int arr[] = new int[n];
		int flagar[] = new int[n];
		int neighbours[] = new int[n];
		int colorar[] = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = Reader.nextInt();
			neighbours[i] = -1;
		}
		DisjointSet ds = new DisjointSet();
		DisjointSet dsc = new DisjointSet();
		ds.makesetBySize(n);
		dsc.makesetBySize(n);

		for (int i = 0; i < m; i++) {
			int t = Reader.nextInt();
			int x = Reader.nextInt();
			int y = Reader.nextInt();

			if (t == 1) {
				arr[x - 1] = y;
			} else if (t == 2) {

				int concomp1 = ds.findBysize(x - 1);
				int concomp2 = ds.findBysize(y - 1);

				if (concomp1 != concomp2) {

					int neigh1 = neighbours[x - 1];
					int neigh2 = neighbours[y - 1];

					int bol1 = flagar[concomp1];
					int bol2 = flagar[concomp2];

					if (neigh1 == neigh2 && neigh1 == -1) {
						ds.unionBySize(x - 1, y - 1);
						colorar[x - 1] = 1;
						colorar[y - 1] = 2;
					} else if (neigh1 == -1) {
						ds.unionBySize(x - 1, y - 1);
						int coll = colorar[dsc.findBysize(neigh2)];
						dsc.unionBySize(neigh2, x - 1);
						colorar[dsc.findBysize(neigh2)] = coll;

					} else if (neigh2 == -1) {
						ds.unionBySize(x - 1, y - 1);
						int coll = colorar[dsc.findBysize(neigh1)];
						dsc.unionBySize(neigh1, y - 1);
						colorar[dsc.findBysize(neigh1)] = coll;
					} else {
						int collx1 = colorar[dsc.findBysize(x - 1)];
						int collx2 = colorar[dsc.findBysize(neigh1)];
						int colly1 = colorar[dsc.findBysize(y - 1)];
						int colly2 = colorar[dsc.findBysize(neigh2)];
						if (collx1 == colly1) {
							//System.out.println(collx1+" "+collx2+" "+colly1+" "+colly2);
							dsc.unionBySize(x - 1, neigh2);
							dsc.unionBySize(y - 1, neigh1);
							colorar[dsc.findBysize(x - 1)] = collx1;
							colorar[dsc.findBysize(y - 1)] = collx2;
							ds.unionBySize(x - 1, y - 1);

						} else {
							//System.out.println(collx1+" "+collx2+" "+colly1+" "+colly2);
							dsc.unionBySize(x - 1, y - 1);
							dsc.unionBySize(neigh1, neigh2);
							colorar[dsc.findBysize(x - 1)] = collx1;
							colorar[dsc.findBysize(neigh1)] = collx2;
							ds.unionBySize(x - 1, y - 1);
						}
					}

					if (bol1 == 1 || bol2 == 1) {
						flagar[ds.findBysize(x - 1)] = 1;
					}
					if (x!=y){
					neighbours[x - 1] = y - 1;
					neighbours[y - 1] = x - 1;}

				} else {

					int col1 = dsc.findBysize(x - 1);
					int col2 = dsc.findBysize(y - 1);
					if (col1 == col2) {
						if (x-1 != y-1)
						flagar[concomp1] = 1;
					}

				}
//				System.out.println();
//				for (int yo : flagar) {
//					System.out.print(yo+" ");
//				}
//				System.out.println();
//				for (int ii=0;ii<n;ii++) {
//					System.out.print((dsc.findBysize(ii)+1)+" "); 
//				}
				
			} else {
				

				
				int v = Reader.nextInt();
				int yoo1 = ds.findBysize(x - 1);
				int yoo2 = ds.findBysize(y - 1);
				if (yoo1 == yoo2 && flagar[yoo1] == 0) {
					long p = ((long)v) *((long) arr[x - 1]);
					long q = (long)arr[y - 1];

					long gcdd = gcd(p, q);
					p = p / gcdd;
					q = q / gcdd;
					int coll1 = dsc.findBysize(x - 1);
					int coll2 = dsc.findBysize(y - 1);
					if (coll1 == coll2) { 
						System.out.println(p + "/" + q);
					} else {
						System.out.println("-" + p + "/" + q);
					}
				} else {
					System.out.println(0);
				}
			}
		}
	}

	public static long gcd(long a, long b) {
		if (a == 0)
			return b;

		return gcd(b % a, a);
	}

}

/** Class for buffered reading int and double values */
class Reader {
	static BufferedReader reader;
	static StringTokenizer tokenizer;

	/** call this method to initialize reader for InputStream */
	static void init(InputStream input) {
		reader = new BufferedReader(new InputStreamReader(input));
		tokenizer = new StringTokenizer("");
	}

	/** get next word */
	static String next() throws IOException {
		while (!tokenizer.hasMoreTokens()) {
			// TODO add check for eof if necessary
			tokenizer = new StringTokenizer(reader.readLine());
		}
		return tokenizer.nextToken();
	}

	static int nextInt() throws IOException {
		return Integer.parseInt(next());
	}

	static double nextDouble() throws IOException {
		return Double.parseDouble(next());
	}
}

class DisjointSet {
	
	public int[] arr;
	public int size;

	
	public void makesetBySize(int size) {
		this.size = size;
		this.arr = new int[size];
		for (int i = 0; i < size; i++) {
			arr[i] = -1;
		}
	}

	public int findBysize(int x) {
		if (x >= size || x < 0) {
			return Integer.MIN_VALUE;
		} else {
			if (arr[x] < 0) {
				return x;
			} else {
				return findBysize(arr[x]);
			}
		}
	}

	
	public void unionBySize(int a, int b) {
		int fa = findBysize(a);
		int fb = findBysize(b);
		if (a >= size || b >= size || a < 0 || b < 0) {
			return;
		}

		if (fa == fb) {

			return;
		} else {
			if (arr[fb] < arr[fa]) { // doubt wtf is this??
				arr[fb] += arr[fa];
				arr[fa] = fb;
			} else {

				arr[fa] += arr[fb];
				arr[fb] = fa;
			}
		}
	}
	
}
