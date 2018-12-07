//package codechef;
import java.beans.Visibility;
import java.io.IOException;
import java.util.ArrayList;
import javax.swing.text.html.MinimalHTMLWriter;
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
class Main {
	public static void main(String[] args) throws IOException{
		Reader.init(System.in);
		int n=Reader.nextInt();
		int m=Reader.nextInt();
		int arr[][]=new int[n][m];
		ArrayList<Integer> unique= new ArrayList();
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) {
				arr[i][j]=Reader.nextInt();
				if (!unique.contains(arr[i][j])) {
					unique.add(arr[i][j]);
				}
			}
		}
		graph graph=new graph(n,m,arr);
		if (unique.size()==1) {
			System.out.println(m*n);
		}
		else{
			int l=unique.size();
			int ans=0;
			for (int i=0;i<l-1;i++) {
				for (int j=i+1;j<l;j++) {
					int yo=graph.bfs(unique.get(i),unique.get(j));
					//System.out.println((unique.get(i))+" "+(unique.get(j))+" "+yo);
					if(ans<yo) {
						ans=yo;
					}
				}
			}
			System.out.println(ans);
		}
		
		
		
	}
}

class graph{
	int n;
	int m;
	int arr[][];
	graph(int n,int m,int[][] a){
		this.n=n;
		this.m=m;
		this.arr=a;
	}
	ArrayList<Integer> giveneighbours(int i,int j){
		ArrayList<Integer> a=new ArrayList();
		if(i+1>=0 && i+1<n && j>=0 && j<m) {
			a.add(i+1);
			a.add(j);
		}
		if(i-1>=0 && i-1<n && j>=0 && j<m) {
			a.add(i-1);
			a.add(j);
		}
		if(i>=0 && i<n && j-1>=0 && j-1<m) {
			a.add(i);
			a.add(j-1);
		}
		if(i>=0 && i<n && j+1>=0 && j+1<m) {
			a.add(i);
			a.add(j+1);
		}
		return a;
	}
	int bfs(int p, int q) {
		boolean[][] bfsarr=new boolean[n][m];
		int maximum=0;
		int kar=0;
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				if(arr[i][j]==p || arr[i][j]==q) {
					if(!(bfsarr[i][j])) {
						kar=bfsvisit(i,j,bfsarr,p,q);
						//System.out.println(kar);
						if(kar>maximum) {
							maximum=kar;
						}
					}
				}
			}
		}
		return maximum;
	}
	int bfsvisit(int i,int j,boolean[][] bfsarr,int r,int s) {
		//bfsarr[i][j]=true;
		ArrayList<Integer> queue=new ArrayList();
		queue.add(i);
		queue.add(j);
		bfsarr[i][j]=true;
		int p=0;
		int q=0;
		int x=0;
		int y=0;
		int count=0;
		ArrayList<Integer> neighbour=new ArrayList();
		while(!(queue.isEmpty())) {
			p=queue.remove(0);
			q=queue.remove(0);
			neighbour=giveneighbours(p, q);
			//bfsarr[p][q]=true;
			count+=1;
			//System.out.println((p+" "+q));
			//ystem.out.println(neighbour);
			while(!(neighbour.isEmpty())) {
				x=neighbour.remove(0);
				y=neighbour.remove(0);
				if(arr[x][y]==r || arr[x][y]==s) {
					if(!(bfsarr[x][y])) {
						queue.add(x);
						queue.add(y);
						bfsarr[x][y]=true;
					}
				}
			}
		}
		return count;
	}
}

//4 4
//1 4 4
//1 2 2
//2 4 1
//1 3 3