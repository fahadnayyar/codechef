package codechef;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

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

class main4 {
	public static void main(String[] args) throws IOException {
		Reader.init(System.in);
		int t = Reader.nextInt();
		for (int w = 0; w < t; w++) {
			int n = Reader.nextInt();
			int q = Reader.nextInt();
			int arr[] = new int[n];
			for (int i = 0; i < n; i++) {
				arr[i] = Reader.nextInt();

			}
			SegmentTreeMax stm = new SegmentTreeMax(n, arr);
			SegmentTreeSum sts = new SegmentTreeSum(n, arr);
			for (int i = 0; i < q; i++) {
				int konsa = Reader.nextInt();
				if (konsa == 1) {
					int l = Reader.nextInt();
					int r = Reader.nextInt();
					long csum = sts.Query(l - 1, r - 1);
					long mode = (long) stm.Query(l - 1, r - 1).ind + 1;
					long median = (long) giveMedian(sts, l - 1, r - 1, csum) + 1;
					// System.err.print(mode+" ");
					// System.err.println(median);
					System.out.println(lcm(mode, median));
				} else {
					int j = Reader.nextInt();
					int x = Reader.nextInt();
					stm.Update(j - 1, x);
					sts.Update(j - 1, x);
				}
			}
		}
	}

	public static double giveMedian(SegmentTreeSum st, int ql, int qr, long csum) {
		if (csum % 2 != 0) {
			csum = (csum+1) / 2;
			int l = ql;
			int r = qr;
			while (l <= r) {
				int mid = (l + r) / 2;
				if (st.Query(ql, mid) >= csum) {
					r = mid - 1;
				} else {
					l = mid + 1;
				}

			}
			return l;
		} else {
			int l1 = ql;
			int r1 = qr;
			long csum1 = csum / 2;
			while (l1 <= r1) {
				int mid = (l1 + r1) / 2;
				if (st.Query(ql, mid) >= csum1) {
					r1 = mid - 1;
				} else {
					l1 = mid + 1;
				}

			}
			long csum2 = (csum+2) / 2;

			int l2 = ql;
			int r2 = qr;
			// long csum1=csum/2;
			while (l2 <= r2) {
				int mid = (l2 + r2) / 2;
				if (st.Query(ql, mid) >= csum1) {
					r2 = mid - 1;
				} else {
					l2 = mid + 1;
				}

			}

			return (l1 + l2) / 2;
		}

	}

	// public static long gcd(long a,long b) {
	// if (a==0 || b==0) {
	// return 0;
	// }
	// else if (a==b){
	// return a;
	// }
	// else {
	// if (a>b) {
	// return gcd(a-b, b);
	// }
	// else {
	// return gcd(a, b-a);
	// }

	// }

	// }
	public static long lcm(long a, long b) {
		// System.out.println(gcd(a, b));
		long yo = a * b;
		long ro = gcd(a, b);
		return yo / ro;
	}

	static long gcd(long a, long b) {
		while (a != b) {
			if (a == 0 || b == 0) {
				break;
			}

			if (a > b)
				a = a - b;
			else
				b = b - a;
		}
		return a;
	}

}

class SegmentTreeMax {
	// public static void main(String[] args) {
	// int arr[]= {24,436,-1352,263,-26,3,-46,26,745,3,753};
	// SegmentTreeMax st = new SegmentTreeMax(arr.length, arr);
	// System.out.println(st.Query(1,4 ));
	// System.out.println(st.Query(3, 8));
	// System.out.println(st.Query(7,10 ));
	// System.out.println(st.Query(1,9 ));
	// System.out.println(st.Query(6, 8));
	// System.out.println(st.Query(3,6 ));
	// System.out.println(st.Query(9,9 ));
	// System.out.println(st.Query(3, 7));
	//
	// }

	public int arr[];
	public node segarr[];
	public int n; // size of array whose seg tree is constructed.

	public SegmentTreeMax(int n, int ar[]) {
		this.segarr = new node[(4 * n) + 1];
		this.n = n;
		this.arr = ar;
		Build();
	}

	private void Build() {
		build(arr, 0, n - 1, 1);
	}

	private void build(int ar[], int l, int r, int ind) { // ar is the array on which rmq is to be done, l=0,r=n-1.ind=1
		if (l > r) {
			return;
		}
		if (l == r) {
			segarr[ind] = new node(l, ar[l]);
			return;
		}
		int mid = (l + r) / 2;
		build(ar, l, mid, 2 * ind);
		build(ar, mid + 1, r, 2 * ind + 1);
		// node left = segarr[2*ind];
		// node right = segarr[2*ind+1];
		if (segarr[2 * ind].compare(segarr[2 * ind + 1])) {
			segarr[ind] = segarr[2 * ind];
		} else {
			segarr[ind] = segarr[2 * ind + 1];
		}

		// segarr[ind]=
		// segarr[ind]=Math.max(left, right);
	}
	// public int givemin(int ql, int qr) {
	// return queryMin(l, r, ind, ql, qr)
	// }

	public node Query(int l, int r) {
		return query(0, n - 1, 1, l, r);
	}

	private node query(int l, int r, int ind, int ql, int qr) { // ind=1,l=0,r=n-1,ql,qr is related to queries.
		if (ql > r || qr < l) {
			return new node(-1, Integer.MIN_VALUE);
		} else {
			if (ql <= l && qr >= r) {
				return segarr[ind];
			} else {
				int mid = (l + r) / 2;
				node left = query(l, mid, 2 * ind, ql, qr);
				node right = query(mid + 1, r, 2 * ind + 1, ql, qr);
				if (left.compare(right)) {
					return left;
				} else {
					return right;
				}
				// return Math.max(left, right);

			}
		}
	}

	public void Update(int i, int val) {
		update(0, n - 1, 1, i, val);
	}

	private void update(int l, int r, int ind, int i, int value) { // i is the index at which this value v is to be
																	// updated.
		if (i < l || i > r) {
			return;
		}
		if (l == r) {
			segarr[ind].freq = value;
			return;

		} else {
			int mid = (l + r) / 2;
			update(l, mid, 2 * ind, i, value);
			update(mid + 1, r, 2 * ind + 1, i, value);
			if (segarr[2 * ind].compare(segarr[2 * ind + 1])) {
				segarr[ind] = segarr[2 * ind];
			} else {
				segarr[ind] = segarr[2 * ind + 1];
			}

			// segarr[ind]=Math.max(segarr[2*ind], segarr[2*ind+1]);
			return;
		}
	}

	public void RangeUpdate(int rl, int rr, int inc) {
		rangeUpdate(0, n - 1, 1, rl, rr, inc);
	}

	private void rangeUpdate(int l, int r, int ind, int rl, int rr, int inc) {
		if (rl > r || rr < l) {
			return;
		}
		if (l == r) {
			segarr[ind].freq = segarr[ind].freq + inc;
			return;
		} else {
			int mid = (l + r) / 2;
			rangeUpdate(l, mid, 2 * ind, rl, rr, inc);
			rangeUpdate(mid + 1, r, 2 * ind + 1, rl, rr, inc);
			if (segarr[2 * ind].compare(segarr[2 * ind + 1])) {
				segarr[ind] = segarr[2 * ind];
			} else {
				segarr[ind] = segarr[2 * ind + 1];
			}

			// segarr[ind]=Math.max(segarr[2*ind], segarr[2*ind+1 ]);
		}
	}
}

class SegmentTreeSum {
	// public static void main(String[] args) {
	// int arr[]= {24,436,-1352,263,-26,3,-46,26,745,3,753};
	// SegmentTreeSum st = new SegmentTreeSum(arr.length, arr);
	// System.out.println(st.Query(1,4 ));
	// System.out.println(st.Query(3, 8));
	// System.out.println(st.Query(7,10 ));
	// System.out.println(st.Query(1,9 ));
	// System.out.println(st.Query(6, 8));
	// System.out.println(st.Query(3,6 ));
	// System.out.println(st.Query(9,9 ));
	// System.out.println(st.Query(3, 7));
	//
	// }

	public int arr[];
	public long segarr[];
	public int n; // size of array whose seg tree is constructed.

	public SegmentTreeSum(int n, int ar[]) {
		this.segarr = new long[(4 * n) + 1];
		this.n = n;
		this.arr = ar;
		Build();
	}

	private void Build() {
		build(arr, 0, n - 1, 1);
	}

	private void build(int ar[], int l, int r, int ind) { // ar is the array on which rmq is to be done, l=0,r=n-1.ind=1
		if (l > r) {
			return;
		}
		if (l == r) {
			segarr[ind] = ar[l];
			return;
		}
		int mid = (l + r) / 2;
		build(ar, l, mid, 2 * ind);
		build(ar, mid + 1, r, 2 * ind + 1);
		long left = segarr[2 * ind];
		long right = segarr[2 * ind + 1];
		segarr[ind] = left + right;
	}
	// public int givemin(int ql, int qr) {
	// return queryMin(l, r, ind, ql, qr)
	// }

	public long Query(int l, int r) {
		return query(0, n - 1, 1, l, r);
	}

	private long query(int l, int r, int ind, int ql, int qr) { // ind=1,l=0,r=n-1,ql,qr is related to queries.
		if (ql > r || qr < l) {
			return 0;
		} else {
			if (ql <= l && qr >= r) {
				return segarr[ind];
			} else {
				int mid = (l + r) / 2;
				long left = query(l, mid, 2 * ind, ql, qr);
				long right = query(mid + 1, r, 2 * ind + 1, ql, qr);
				return left + right;
			}
		}
	}

	public void Update(int i, int val) {
		update(0, n - 1, 1, i, val);
	}

	private void update(int l, int r, int ind, int i, int value) { // i is the index at which this value v is to be
																	// updated.
		if (i < l || i > r) {
			return;
		}
		if (l == r) {
			segarr[ind] = value;
			return;

		} else {
			int mid = (l + r) / 2;
			update(l, mid, 2 * ind, i, value);
			update(mid + 1, r, 2 * ind + 1, i, value);
			segarr[ind] = segarr[2 * ind] + segarr[2 * ind + 1];
			return;
		}
	}

	public void RangeUpdate(int rl, int rr, int inc) {
		rangeUpdate(0, n - 1, 1, rl, rr, inc);
	}

	private void rangeUpdate(int l, int r, int ind, int rl, int rr, int inc) {
		if (rl > r || rr < l) {
			return;
		}
		if (l == r) {
			segarr[ind] = segarr[ind] + inc;
			return;
		} else {
			int mid = (l + r) / 2;
			rangeUpdate(l, mid, 2 * ind, rl, rr, inc);
			rangeUpdate(mid + 1, r, 2 * ind + 1, rl, rr, inc);
			segarr[ind] = segarr[2 * ind] + segarr[2 * ind + 1];
		}
	}
}

class node {
	int ind;
	int freq;

	public node(int ind, int freq) {
		this.ind = ind;
		this.freq = freq;
	}

	public boolean compare(node yo) {
		if (this.freq > yo.freq) {
			return true;
		} else if (this.freq < yo.freq) {
			return false;
		} else {
			return this.ind > yo.ind;
		}
	}
}
