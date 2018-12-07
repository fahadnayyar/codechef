//package abcd;

import java.io.IOException;
import java.io.IOException;
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import javax.print.DocFlavor.READER;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
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
	public static void main(String args[])throws IOException {
		Reader.init(System.in);
		int t=Reader.nextInt();
		for(int i=0;i<t;i++) {
			int n=Reader.nextInt();
			double arr[]=new double[n];
			avltree av=new avltree();
			for(int j=0;j<n;j++) {
				av.root=av.insert(av.root, Reader.nextDouble());
			}
			//av.printlist(av.root);
			for(int j=0;j<n-1;j++) {
				//System.out.println(j);
				double a=av.givemaximum(av.root);
				av.root=av.delete(av.root, a);
				double b=av.givemaximum(av.root);
				av.root=av.delete(av.root, b);
				//double b=av.givemaximum(av.root);
				double x=(a+b)/2;
				av.root=av.insert(av.root, x);
				//System.out.println(a+" "+b);
			}
			System.out.println(av.root.data);
		}
	}
}
class Node {
	Node left;
	Node right;
	double data;
	int height=-1;
}
class avltree {
	Node root;
	public double givemaximum(Node a) {
		if(a==null) {
			return -1;
		}
		else if(a.right!=null) {
			return givemaximum(a.right);
		}
		else {
			double x=a.data;
			//delete(a, a.data);
			return x;
		}
		
	}
	int height(Node a) {
		int count=0;
		while(a!=null) {
			a=a.left;
			count+=1;
		}
		return count;
	}
	Node RightRotate(Node a) {
		Node b=a.left;
		a.left=a.left.right;
		b.right=a;
		a.height=maximum(height(a.left),height(a.right))+1;
		b.height=maximum(height(b.left),height(b.right))+1;
		return b;
	}
	int isAVL(Node a) {
		if(a==null)
			return 0;
		if(a.left==null && a.right==null)
			return 0;
		if(a.left!=null && a.right==null)
			return a.left.height;
		if(a.right!=null && a.left==null)
			return a.right.height;
		return a.left.height-a.right.height;
	}
	public Node LeftRotate(Node a) {
		Node b=a.right;	
		a.right=a.right.left;
		b.left=a;
		a.height=maximum(height(a.left),height(a.right))+1;
		b.height=maximum(height(b.left),height(b.right))+1;
		return b;
	}
	public int maximum(int a,int b) {
		if(a>b) {return a;}
		else {return b;}
	}
	Node insert (Node a,double data) {
		if(a==null) {
			a=new Node();
			a.data=data;
			a.height=0;
			return a;
		}
		
		if(a.data>data) {
			a.left=insert(a.left,data);
			int balance=isAVL(a);
			if(balance==2) {
				if(a.left.data>data) {
					
					return RightRotate(a);
				}
				else if(a.left.data<data){
					return DoubleLeftRotate(a);
				}
			}
		}
		if(a.data<=data) {
			a.right=insert(a.right,data);
			int balance=isAVL(a);
			if(balance==-2) {
				if(a.right.data>data) {
					return DoubleRightRotate(a);
				}
				else if(a.right.data<data) {
					return LeftRotate(a);
				}
			}
		}

		
		a.height=maximum(height(a.left),height(a.right))+1;
		return a;
	}
	Node DoubleLeftRotate(Node a) {
		a.left=LeftRotate(a.left);
		return RightRotate(a);
	}
	Node DoubleRightRotate(Node a) {
		a.right=RightRotate(a.right);
		return LeftRotate(a);
	}
	Node delete(Node a,double data) {
		if(a==null) {
			return a;
		}
		if(a.data<data) {
			a.right=delete(a.right,data);

		}
		else if(a.data>data) {
			a.left=delete(a.left,data);
		}
		else {
			if(a.left==null) {
				return a.right;
			}
			else if(a.right==null) {
				return a.left;
			}
			else {
				Node mini=minvalue(a.left);
				double d=mini.data;
				//a.data=mini.data;
				a.left=delete(a.left,data);
				a.data=d;
			} 	
		}
		if(a==null) {
			return null;
		}
		a.height=maximum(height(a.left), height(a.right))+1;
		int balance=isAVL(a);
		if(balance>=2) {
			//System.out.println(isAVL(a.left));	
			if(isAVL(a.left)>=1) {
				return RightRotate(a);
			}
			else if(isAVL(a.left)<=-1){
				return DoubleLeftRotate(a);
			}
		}
		else if(balance<=-2) {	
			//System.out.println(isAVL(a.right));
			if(isAVL(a.right)<=-1) {
				return LeftRotate(a);

			}
			else if(isAVL(a.right)>=1){
				return DoubleRightRotate(a);
			}
		}
		return a;
	}
	Node minvalue(Node a){
		if(a==null) {
			return a;
		}else if(a.right==null){
			return a;
		}
		else{
			return minvalue(a.right);
		}
	}
	public static void printlist(Node a) {
		if (a!=null) {
			printlist(a.left);
			//System.out.print(a.data+" ");
			printlist(a.right);
		}
	}
	
}