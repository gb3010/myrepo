#!/usr/local/bin/python3

#Function to count the number of occurences of a name
def count_occur(name,arr,count=0):
	for i in arr[0:20]:
		if name in i:
			count+=1
	return(count)

#Function to generate unique combinations and ensures uniform distribution of values
def rand_combo_gen():
  import random

  #List with all possible combinations
  a=['john:shane','john:mike','john:robert','john:matt','john:david','john:peter','shane:john','shane:mike','shane:robert','shane:matt','shane:david','shane:peter','mike:john','mike:shane','mike:robert','mike:matt','mike:david','mike:peter','robert:john','robert:shane','robert:mike','robert:matt','robert:david','robert:peter','matt:john','matt:shane','matt:mike','matt:robert','matt:david','matt:peter','david:john','david:shane','david:mike','david:robert','david:matt','david:peter','peter:john','peter:shane','peter:mike','peter:robert','peter:matt','peter:david']
  y=[]
  z=[]

  #Logic to select random value and not repeat the same value
  r=random.choice(a)

  for i in range(70):
      
      
      p1=r.split(':')[0]
      p2=r.split(':')[1]
      r2=random.choice(a)
      while p1 not in r2 and p2 not in r2:
          r=r2
          y.append(r)
          break
  
  #Code block to filter out and save only unique values
  for i in y:
  	while i not in z:
  		z.append(i)
  
  
  q=z[0:20] #Fetch the first 20 values
  
  #Code block to count the number of occurences of each name
  gc=count_occur('john',q)
  bc=count_occur('peter',q)
  sc=count_occur('shane',q)
  vic=count_occur('mike',q)
  vec=count_occur('robert',q)
  kc=count_occur('matt',q)
  sec=count_occur('david',q)
  
  count_list=[]
  
  for i in gc,bc,sc,vic,vec,kc,sec:
  	count_list.append(i)
  
  
  #Code block to calculate the average of the count of number of occurences
  sum=0
  
  for i in count_list:
  	sum+=i
  
  avg=round(sum/len(count_list),2)
 
  #Saving the variance value between average and count in a list
  diff=[] #list to save diff values
  for i in count_list:
  	diff.append(round((i-avg),2))
  
  #Checking for values which deviate from the expected range and flipping the flag value accordingly
  flag=1
  
  for i in diff:
  	if i <= -1 or i>1:
  	  flag*=0
 
  #Saving the values in human readable format
  readable=[]
  for i in q:
  	readable.append("Requests: " + i.split(':')[0].title() + " ; " + "Incidents: " + i.split(':')[1].title())

  
  #Returning the output list to main()
  if flag == 1:
  	return(readable)


def main():
    for i in range(100):
    
    	output=rand_combo_gen()
    	if output is not None:
    		#print(output)
    		#print(output)
    		print(' | '.join(output[0:5]))
    		print(' | '.join(output[5:10]))
    		print(' | '.join(output[10:15]))
    		print(' | '.join(output[15:20]))
    		break


main()