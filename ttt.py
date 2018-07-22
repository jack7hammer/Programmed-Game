import numpy as np
import os

#filling the 2d array with spaces
m=np.array(([' ',' ',' '],[' ',' ',' '],[' ',' ',' ']))

#this function marks either X or O in the matrix
def mark(x,y,b):
	if(m[x,y])!=' ':
		return 1
	m[x,y]=b
	return 0

#here is the main function where we take inputs and all 
def main():
	global w
     #maximum 9 moves
	for i in range (9):
		#j variable for knowing wether it is player 1 or player 2's tuen
		j = (i%2)

		#printing the GUI along with values
		print("\n   1   2   3 \n")
		for k in range (3):
			n=k+1

			print(n,(" "+m[k,0] + " | " +m[k,1]+" | "+m[k,2]))

			if k == 2:
				break
			print("  -----------")
		print("\n")

        #if J is even then it is player 1's turn
		if j == 0:
			print("Player 1 : ")
			l =list(map(int,input().split()))
			while(l[0]>3 or l[1]>3):
				print("invalid input")
				l=list(map(int,input().split()))
            
            #checking wether the block is already filled or not 
			while mark(l[0]-1,l[1]-1,'X'):
				#if it is filled then we say  ...you cant mark here 
				print("Cant mark here")
				l =list(map(int,input().split()))
			#else we mark it 
			mark(l[0]-1,l[1]-1,'X')

            #we check wether player 1 wins in this turn or not 
			if (win('X')):
				w=1  # if he wins we set the value as 1 
				break

		#if j is odd then it is player 2's turn and same as player 1's algo just that if p2 wins we set w=2
		else:
			print("Player 2 : ")
			l  =list(map(int,input().split()))
			while(l[0]>3 or l[1]>3):
				print("invalid input")
				l=list(map(int,input().split()))
			while mark(l[0]-1,l[1]-1,'O'):
				print("cant mark here")
				l = list(map(int,input().split()))
			mark(l[0]-1,l[1]-1,'O')
			if win('O'):
				w=2
				break
		unusedvar=os.system('cls') #clearing the previous GUI so the new one is at the right spot 

#win function		
def win(u):
	for j in range(3):

	    for i in range(3):  #every '|' in between is a seperation between conditions
	    	if (m[j%3,i%3]==u)&(m[j%3,(i+1)%3]==u) &((m[j%3,(i+2)%3])==u) |(m[j%3,(i+j)%3]==u)& (m[(j+1)%3,(i+j)%3]==u) & (m[(j+2)%3,(i+j)%3]==u) |(m[0,0]==u)&(m[1,1]==u) &  (m[2,2]==u) | (m[0,2]==u) &(m[1,1]==u)&(m[2,0]==u):
	    		return 1
		
			
			

	
main()
unusedvar= os.system('cls')
if(w==2):
	print("Player 2 is the winner ! \n ")
if(w==1):
	print("Player 1 is the winner ! \n")
if(w==0):
	print("Draw!! \n")
for k in range (3):
			n=k+1

			print(("  "+m[k,0] + " | " +m[k,1]+" | "+m[k,2]))

			if k == 2:
				break
			print(" -----------")
print("\n")


print("Press Enter to end")
s = input()