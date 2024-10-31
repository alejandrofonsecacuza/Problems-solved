)
def solve(B, C, k):
	B=list(filter(lambda x:x<=k, B)) 
	C=list(filter(lambda x:x<=k, C))
	B.sort();
	C.sort(reverse=True);
	index=0;
	count=0;
	for bi in range(len(B)):
		for ci in range(index,len(C)):
			if B[bi]+C[ci]>k:
				 index+=1;
			else:
				 count+=1;
	return count
				 
				
		
		
				
	

t=int(input())
while(t):
	B=[];
	C=[];
	t-=1;
	n, m, k=map(int, input().split())
	B=list(map(int, input().split()))
	C=list(map(int, input().split()))
	print(solve(B, C, k));

	