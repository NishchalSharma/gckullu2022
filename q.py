# Developed by Nishchal Sharma
#----------------------------------------------------------------
#------- A very Dirty Code for A very Dirty Work
#-------- Many Revisions- ----------------------------------------
#------- Dont Try to Edit, ----
#------- --------------------------------------------

import time
import math
import os
import sys
import shutil
import pathlib

#---- This Class Manages Seats of a Course, Automatically calculates the no of seats reserved
class seats:
    coursename=""
    #----- currently allotted seats
    cid=0
    gen=0
    sc=0
    st=0
    sports=0
    culture=0
    ph=0
    sgc=0
    xgen=0 #-- a fancy name for EWS 
    #--------Following seats are the maximum seats
    m_gen=0
    m_sc=0
    m_st=0
    m_sports=0
    m_culture=0
    m_ph=0
    m_sgc=1
    m_xgen=0
    def __init__(self,n,id,max_seats):
        self.coursename=n
        self.cid=id
        self.m_sc=int(round(max_seats*0.15)) # 15% SC
        self.m_st=int(round(max_seats*0.075)) # 7.5 % ST
        self.m_sports=int(round(max_seats*0.05)) # 5% sports
        self.m_culture=int(round(max_seats*0.05)) # 5% cultural
        self.m_ph=int(round(max_seats*0.05))  # 5% divyang
        self.m_xgen=int(round(max_seats*0.10)) # 10% EWS
        self.m_gen=max_seats-self.m_sc-self.m_st-self.m_sports-self.m_culture-self.m_ph-self.m_xgen # remaining seats for general
    
    def adjust(self): # -- code that recalculates the seats if any seat is vacant by assigning it to general pool. a very crucial function 
        if(self.remain()>0):
            if(self.sc<self.m_sc):
                self.m_gen+=(self.m_sc-self.sc)
                self.m_sc=self.sc

            if(self.st<self.m_st):
                self.m_gen+=(self.m_st-self.st)
                self.m_st=self.st
            if(self.sports<self.m_sports):
                self.m_gen+=(self.m_sports-self.sports)
                self.m_sports=self.sports
            if(self.culture<self.m_culture):
                self.m_gen+=(self.m_culture-self.culture)
                self.m_culture=self.culture
            if(self.ph<self.m_ph):
                self.m_gen+=(self.m_ph-self.ph)
                self.m_ph=self.ph
            if(self.xgen<self.m_xgen):
                self.m_gen+=(self.m_xgen-self.xgen)
                self.m_xgen=self.xgen
            
        self.gen=0
        self.sc=0
        self.st=0
        self.sports=0
        self.culture=0
        self.ph=0
        self.sgc=0
        self.xgen=0


    def status(self):# prints status for a given subject
        print("------------------------------------------------------------------------------------------")
        print(""+self.coursename+" || Gen="+str(self.gen)+"/"+str(self.m_gen)+" SC="+str(self.sc)+"/"+str(self.m_sc)+" ST="+str(self.st)+"/"+str(self.m_st)+" SPORTS="+str(self.sports)+"/"+str(self.m_sports)+" CULTURE="+str(self.culture)+"/"+str(self.m_culture)+" PH="+str(self.ph)+"/"+str(self.m_ph)+" SGC="+str(self.sgc)+"/"+str(self.m_sgc)+" EWS="+str(self.xgen)+"/"+str(self.m_xgen))
        print("Total Vacant Seats="+str(self.remain()))
        print("________________________________________________________________________________________")
        '''
    def status(self):
        print("---"+self.coursename+"---")
        print("Gen seats:"+str(self.gen)+"/"+str(self.m_gen))
        print("SC seats:"+str(self.sc)+"/"+str(self.m_sc))
        print("ST seats:"+str(self.st)+"/"+str(self.m_st))
        print("SPORTS seats:"+str(self.sports)+"/"+str(self.m_sports))
        print("Culture seats:"+str(self.culture)+"/"+str(self.m_culture))
        print("Physically Handicapped seats:"+str(self.ph)+"/"+str(self.m_ph))
        print("Single Girld Child seats:"+str(self.sgc)+"/"+str(self.m_sgc))
        print("Total Vacant Seats="+str(self.remain()))
        print("------------------------")
        '''
    def remain(self): # calculates remaining  seats . it will be used to adjust any remaining seats and will help in converting it to general seats
         return(self.m_gen+self.m_sc+self.m_st+self.m_sports+self.m_culture+self.m_ph+self.m_xgen-self.gen-self.sc-self.st-self.sports-self.culture-self.ph-self.xgen)

#----- This is a Model for A Single Candidate will be used to allot seat
class candidate():
    cname=""
    father=""
    mother=""
    dob=""
    phone=""
    gender=""
    sports=False
    category=""
    culture=False
    sgc=False
    ph=False
    ews=False

    marks=0
    x1="" # Preference 1
    x2="" # Preference 2
    x3="" # Preference 3
    x4="" # Preference 4
    x5="" # Preference 5
    #-- above code workls for max 5 preferences only, if more preferences are needed suitable changes is to be done.
    
    def __init(self):
        pass
    def isst(self): # returns true if student is ST
        if(self.category=='ST'):
            return True
    def issc(self): # returns true if student is SC
        if(self.category=='SC'):
            return True
    def isxgen(self): # returns true if student is EWS
        return self.ews
    
    def issports(self): # returns true if student is Sports
            return(self.sports)
    def isculture(self): # returns true if student is cultural
        return(self.culture)
    def issgc(self): # returns true if student is Single girl child
        return(self.sgc)
    def isph(self): # returns true if student is divyang
        return(self.ph)


#---- This is all seats data
#------ Changes here will reflect in final allotments
#----- Name of the seat should match in CSV
#---- Last integer is no of seats.
#--- set seats to 0 if you dont want to allott any seats to a given subject
        
s1=seats("Maths BSC",1,100)
s2=seats("Mathematics BA",2,80)
s3=seats("Physics",3,100)
s4=seats("Chemistry",4,100)
s5=seats("Computer Science",5,0)
s6=seats("Zoology",6,100)
s7=seats("Botany",7,100)
s8=seats("Geography BSC",8,0)
s9=seats("Geography BA",9,100)
s10=seats("",10,0)

a1=seats("English",10,80)
a2=seats("Hindi",11,100)
a3=seats("Sanskrit",12,100)
a4=seats("History",13,120)
a5=seats("Pol Science",14,120)
a6=seats("Public Ad",15,100)
a7=seats("Music Vocal",16,80)
a8=seats("Music Instrumental",17,40)
a9=seats("Sociology",18,80)
a10=seats("J&MC",19,80)
a11=seats("Economics",20,100)
a12=seats("B.COM",21,140)
a13=seats("Physical Education",22,100)
a14=seats("Tourism & Travel Mangt.",23,100)
a15=seats("Education",24,80)
a16=seats("Geology",25,0)
#--------for 2023
a17=seats("BCA",26,0)
a18=seats("BBA",27,0)
a19=seats("B.Voc.(Hospitality and Tourism)",28,40)
a20=seats("B.Voc.(Retail Management)",29,40)

#---------------------------------

#----- This is a hashmap of Above seat for faster Lookup ----------

allseats={"BCA":a17,"BBA":a18,"B.Voc.(Hospitality and Tourism)":a19,"B.Voc.(Retail Management)":a20,"Maths":s1,"Mathematics":s2,"Physics":s3,"Chemistry":s4,"Computer Science":s5,"Zoology":s6,"Botany":s7,"Geography BSC":s8,"Geography":s9,"":s10,"English":a1,"Hindi":a2,"Sanskrit":a3,"History":a4,"Political Science":a5,"Public Administration":a6,"Music Vocal":a7,"Music Instrumental":a8,"Sociology":a9,"Journalism & Mass Comm.":a10,"Economics":a11,"B.Com.":a12,"Physical Education":a13,"Tourism & Travel Mangt.":a14,"Education":a15,"Geology":a16}

# this allots a seat in a given course, applies the Reservation system also, very handy and powerful
def allotone(id,c,p):
    s=allseats[id]  
    
    if(s.gen<s.m_gen):
        log (str(c.id)+","+c.cname+","+c.father+","+c.mother+","+c.marks+","+allseats[id].coursename+",Open "+str(s.gen+1)+" Preference no "+str(p),allseats[id].coursename)
        s.gen+=1
        return True
    elif (c.isst()):
        if(s.st<s.m_st):
           log (str(c.id)+","+c.cname+","+c.father+","+c.mother+","+c.marks+","+allseats[id].coursename+",ST "+str(s.st+1)+" Preference no "+str(p),allseats[id].coursename)
           s.st+=1
           return True
    elif (c.issc()):
        if(s.sc<s.m_sc):
            log (str(c.id)+","+c.cname+","+c.father+","+c.mother+","+c.marks+","+allseats[id].coursename+",SC"+str(s.sc+1)+" Preference no "+str(p),allseats[id].coursename)
            s.sc+=1
            return True
    elif (c.issports()):
        if(s.sports<s.m_sports):
            log (str(c.id)+","+c.cname+","+c.father+","+c.mother+","+c.marks+","+allseats[id].coursename+",Sports"+str(s.sports+1)+" Preference no "+str(p),allseats[id].coursename)
            s.sports+=1
            #print("Sports  seat allotted")
            return True
    elif (c.isculture()):
        if(s.culture<s.m_culture):
            log (str(c.id)+","+c.cname+","+c.father+","+c.mother+","+c.marks+","+allseats[id].coursename+",Culture "+str(s.culture+1)+" Preference no "+str(p),allseats[id].coursename)
            s.culture+=1
            #print("culture  seat allotted")
            return True
    elif (c.isph()):
        if(s.ph<s.m_ph):
            log (str(c.id)+","+c.cname+","+c.father+","+c.mother+","+c.marks+","+allseats[id].coursename+",PH  "+str(s.ph+1)+" Preference no "+str(p),allseats[id].coursename)
            s.ph+=1
            #print("ph  seat allotted")
            return True
    
    elif (c.isxgen()):
        if(s.xgen<s.m_xgen):
            log (str(c.id)+","+c.cname+","+c.father+","+c.mother+","+c.marks+","+allseats[id].coursename+",EWS "+str(s.xgen+1)+" Preference no "+str(p),allseats[id].coursename)
            s.xgen+=1
            #print("###"+c.cname+" >>EWS>>Allotted")
            return True
    elif (c.issgc()):
        if(s.sgc<s.m_sgc):
            log (str(c.id)+","+c.cname+","+c.father+","+c.mother+","+c.marks+","+allseats[id].coursename+",SGC  "+str(s.sgc+1)+" Preference no "+str(p),allseats[id].coursename)
            s.sgc+=1
           # print("sgc  seat allotted")
            return True
    else:
        #log ("******"+","+c.cname+","+allseats[id].coursename+",**Not Alloted **")
        return False
def log(x,course):
      # print(x)
       f=open('allot.csv','a') # this is the file which will be used to create allotment list. 
       #//--- lets create directory
       # will create directory for each course and will save individual allottment there.
       pathlib.Path("allsubjects/"+course).mkdir(parents=True, exist_ok=True) 
       f2=open("allsubjects/"+course+"/allot.csv",'a+')
       f.write(x)
       f.write("\n")
       f2.write(x)
       f2.write("\n")
def clearfile():
    open('allot.csv', 'w').close()
    # remove allsubjects folder tree
    shutil.rmtree('allsubjects')
    
def adjustseats(): # adjusts seats if any vacant seat is there.
    for (seats,value) in allseats.items():
        value.adjust()
        
#--- This is a fast roller for allottment, checks if seats are still available and reshuffles the seats and starts again, saves my time ;)
def roll(v=12):# assign a higher value like 20 for even better result.
    for i in range(1,v):
        clearfile()
        start()
        adjustseats()
        
        
# this is the allot starter , this requires a well formatted a.csv and will create a allot.csv, make sure that a.csv should be arranged accoding to merit, otherwise......
def start():
    
    sn=0
    na=0
    print("Opening File !!!")
    i=open('a.csv','r',errors='ignore')
    
    print("\n\n>>>>>>>>>>> Roster System Initializing >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("---- System Running -----")
    t1=time.time() # time stamp to measure performance
    for lines in i:
        lines=lines.rstrip('\n')
        lines=lines.rstrip('\r')
        v=lines.split(",")
        #--------------the magic begins here---------------
        loop_counter=len(v)-10
        #------------ the magic line ----------------------
        c=candidate()
        c.id=v[0]
        c.cname=v[1]
        c.father=v[2]
        c.mother=v[3]
        c.dob=v[4]
        #c.phone=v[5]
        c.gender=v[5]
        c.category=v[6]
        # - the sports , cultural.
        if(v[7]=='Sports'):
            c.sports=True
            #print("Sports Category printer="+v[8])
        else:
            c.sports=False

        if(v[7]=='Cultural'):
            c.culture=True
        else:
            c.culture=False
        
        if(v[7]=='Economic Weaker Section' or v[7]=='IRDP/BPL'):
            #print("\n>>"+v[1]+">>"+v[7]+">>"+v[10])
            c.ews=True
        else:
            c.ews=False

        if(v[7]=='PWD'):
            c.ph=True
        else:
            c.ph=False
        
        if(v[8]=='TRUE' or v[8]=='Yes'):
            c.sgc=True
        else:
            c.sgc=False

        
        
        #c.category=v[9]
        
        c.marks=v[9]
        """
        c.x1=v[13]
        c.x2=v[14]
        c.x3=v[15]
        c.x4=v[16]  
        c.x5=v[17]  
        
        #print("loop counter",loop_counter)
        for x in range(1,loop_counter+1):
            #print("v index:",12+x)
            if(allotone(v[12+x],c,x)):
                sn+=1
            else:
                log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
                na+=1
        """
        # a very stupid way to allot seats, This can be improved.... if I get time.
        # for Now it works, ugly , but works
        if loop_counter==1:
            if (allotone(v[10],c,1)):
                sn+=1
            else:
                log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
                na+=1

        if loop_counter==2:
            if (allotone(v[10],c,1)):
                sn+=1
            elif(allotone(v[11],c,2)):
                sn+=1
            else:
                log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
                na+=1

        if loop_counter==3:
            if (allotone(v[10],c,1)):
                sn+=1
            elif(allotone(v[11],c,2)):
                sn+=1
            elif(allotone(v[12],c,3)):
                sn+=1
            else:
                log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
                na+=1

        if loop_counter==4:
            if (allotone(v[10],c,1)):
                sn+=1
            elif(allotone(v[11],c,2)):
                sn+=1
            elif(allotone(v[12],c,3)):
                sn+=1
            elif(allotone(v[13],c,4)):
                sn+=1
            else:
                log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
                na+=1

        if loop_counter==5:
            if (allotone(v[10],c,1)):
                sn+=1
            elif(allotone(v[11],c,2)):
                sn+=1
            elif(allotone(v[12],c,3)):
                sn+=1
            elif(allotone(v[13],c,4)):
                sn+=1
            elif(allotone(v[14],c,5)):
                sn+=1
            else:
                log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
                na+=1
        if loop_counter==6:
            if (allotone(v[10],c,1)):
                sn+=1
            elif(allotone(v[11],c,2)):
                sn+=1
            elif(allotone(v[12],c,3)):
                sn+=1
            elif(allotone(v[13],c,4)):
                sn+=1
            elif(allotone(v[14],c,5)):
                sn+=1
            elif(allotone(v[15],c,6)):
                sn+=1
            else:
                log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
                na+=1

        if loop_counter==7:
            if (allotone(v[10],c,1)):
                sn+=1
            elif(allotone(v[11],c,2)):
                sn+=1
            elif(allotone(v[12],c,3)):
                sn+=1
            elif(allotone(v[13],c,4)):
                sn+=1
            elif(allotone(v[14],c,5)):
                sn+=1
            elif(allotone(v[15],c,6)):
                sn+=1
            elif(allotone(v[16],c,7)):
                sn+=1
            else:
                log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
                na+=1

        if loop_counter==8:
            if (allotone(v[10],c,1)):
                sn+=1
            elif(allotone(v[11],c,2)):
                sn+=1
            elif(allotone(v[12],c,3)):
                sn+=1
            elif(allotone(v[13],c,4)):
                sn+=1
            elif(allotone(v[14],c,5)):
                sn+=1
            elif(allotone(v[15],c,6)):
                sn+=1
            elif(allotone(v[16],c,7)):
                sn+=1
            elif(allotone(v[17],c,8)):
                sn+=1
            else:
                log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
                na+=1
        if loop_counter==9:
            if (allotone(v[10],c,1)):
                sn+=1
            elif(allotone(v[11],c,2)):
                sn+=1
            elif(allotone(v[12],c,3)):
                sn+=1
            elif(allotone(v[13],c,4)):
                sn+=1
            elif(allotone(v[14],c,5)):
                sn+=1
            elif(allotone(v[15],c,6)):
                sn+=1
            elif(allotone(v[16],c,7)):
                sn+=1
            elif(allotone(v[17],c,8)):
                sn+=1
            elif(allotone(v[18],c,9)):
                sn+=1
            else:
                log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
                na+=1

                
                """
        if(allotone(v[13],c,1)):
           sn+=1
        elif(allotone(v[14],c,2)):
           sn+=1
        elif(allotone(v[15],c,3)):
           sn+=1
        elif(allotone(v[16],c,4)):
           sn+=1
        elif(allotone(v[17],c,5)): # if more then 5 choices are to be used , add one more allottment line
           sn+=1
        else:
           # there is a chance some students will not be allotted to any preferences because of their marks. note them down in file.
           log("ID="+v[0]+","+str(v[1])+","+c.father+","+c.mother+","+str(c.marks)+",******All Preferences Full  allocation failed *****,first preference:"+str(v[13])+" 2nd preference:"+v[14]+" 3rd preference:"+v[15],"notallotted")
           na+=1
           """
    t2=time.time()
    unallotted=0
    for s in allseats.values():
       s.status()
    for k in allseats.values():
       unallotted+=k.remain()
    print('Total Seats available='+str(unallotted))
    
    print("---Total -->>"+str(sn)+" Students Allotted")
    print("---Total -->>"+str(na)+" Students NOT Allotted")
    print("---Total -->>"+str(sn+na)+" Students")
    print("----Allocation System Finished-----")
    print("---- Total time Taken="+str(t2-t1)+" seconds")
    i.close()
#---start the script---
roll()
