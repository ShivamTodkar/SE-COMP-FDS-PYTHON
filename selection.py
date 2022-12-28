def accept_array(A):
     n=int(input("Enter the total no of students:"))
     for i in range(n):
          x=float(input("Enter the first year percentage of students %d:"%(i+1)))
          A.append(x)
          print("Array accepted successfully\n\n")

def display_array(A):
     n=len(A)
     if(n==0):
          print("\n no records in the daqtabase")
     else:
              for i in range (n):
          	          print("\n")

def selection_sort(A):
     n=len(A)
     for pos in range(n-1):
          mid_ind=pos
          for i in range(pos+1,n):
               if(A[i]<A[mid_ind]):
                    mid_ind=i
                    temp=A[pos]
                    A[pos]=A[mid_ind]
                    A[mid_ind]=temp

def bubble_sort(A):
     n=len(A)
     for Pass in range(1,n):
          for i in range(n-Pass):
               if(A[i]<A[i+1]):
                    temp=A[i]
                    A[i]=A[i+1]
                    A[i+1]=temp

def main():
     A=[]
     while True:
          print("\t1:Accept & Display the FE marks")
          print("\t2:Selection sort Acsending order")
          print("\t3:Bubble sort Descending order and display top five scores")
          print("\t4:Exit")
          ch=int(input("Enter the choice:"))
          if(ch==1):
               accept_array(A)
               display_array(A)
          elif(ch==2):
               print("\Marks before sorting")
               display_array(A)
               selection_sort(A)
               print("\Marks after sorting")
               display_array(A)
          elif(ch==3):
               print("\Marks before sorting")
               display_array(A)
               bubble_sort(A)
               print("\Marks after sorting")
               display_array(A)
          if(len(A)>=5):
               print("Top five scoresa:")
               for i in range(5):
                    print("\t%.2f"%A[i])
          elif(ch==4):
               print("End of program")
               break
          else:
               print("Wrong choice Entered!!TRY AGAIN")
main()
