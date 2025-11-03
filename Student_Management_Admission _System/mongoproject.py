import pymongo;
try:
    client = pymongo.MongoClient("mongodb+srv://student_admission:student0987@cluster0.yr69ymz.mongodb.net/",
                                 tlsAllowInvalidCertificates=True)
    client.admin.command('ping')
    print("Connected to MongoDB")
except Exception as e:
    print("Error connecting to MongoDB:", e)

db=client["ducat_users"];
coll=db.students;
coll1=db.placed_students;

def admission(id,name,course,duration):
    coll.insert_one({"id":id,"name":name,"course":course,"duration(months)":duration,"status":"Incomplete"});

def total():
    for data in coll.find():
        print(f"Ducat_Id:{data["id"]} Name:{data["name"]} Course:{data["course"]} Status:{data["duration"]}");
        print("-------------------------------------------------------------")

def data_remove(id):
    coll.delete_one({"id":id});

def student_acc_course(course):
    return coll.count_documents({"course":course});

def certificate_collection(id):
    for data in coll.find({"id":id}):
        if(data["status"]=="Completed"):
            print("You are Valid For Certificate. Please Visit to Reception.");
        else:
            print("Not Completed/Updated the course.Talk To counsellor.");

def update_status(id):
    coll.update_one({"id":id},{"$set":{"status":"Completed"}});

def data_extraction():
    print("Press 21 if Want data according to ID");
    print("Press 22 if Want data according to Name");
    print("Press 23 if Want data according to Course");

    dataInp=int(input("Enter the choiice:"));
    if(dataInp==21):
        data1=int(input("Enter id:"))
        for el in coll.find({"id":data1}):
            print(el);
    elif(dataInp==22):
        data2=input("Enter name:")
        for el in coll.find({"name":data2}):
            print(el);
    elif(dataInp==23):
        data3=input("Enter course:")
        for el in coll.find({"course":data3}):
            print(el);
    else:
        print("Invalid Input")
def sorted_data():
    for el in coll.find().sort({"name":1}):
        print(el);
def update_course(id,course):
    coll.update_one({"id":id},{"$set":{"course":course}});
def add_course(id,add_cou):
    coll.update_one({"id":id},{"$push":{"course":add_cou}});
def string_to_array(col_name):
    coll.update_many({},{"$set":{col_name:["$"]}});

def main():
    print("Press 1 for new student");
    print("Press 2 for see all the data");
    print("Press 3 for remove the student");
    print("Press 4 for count of student according to course");
    print("Press 5 for certificate Collection");
    print("Press 6 for update status");
    print("Press 7 for Data Extraction");
    print("Press 8 for Sorted Data");
    print("Press 9 for Change the course")
    print("Press 10 for Add a Course")
    print("Press 11 for String to Array");
    print("Press 0 for exit");

    choice=int(input("Enter your Choice:"));
    while(True):
        if(choice==0):
            break;

        elif(choice==1):
            st_id =int(input("Enter Your id:"))
            name=input("Enter Name:")
            course=input("Enter Course Name:")
            duration=int(input("Enter Duration:"))
            admission(st_id,name,course,duration);
            print("Data Inserted");
            break;
        elif(choice==2):
            total();
            break;
        elif(choice==3):
            id=int(input("Enter id:"));
            data_remove(id);
            print("Data Removed")
            break;
        elif(choice==4):
            st_course=input("Enter the course:");
            print(f"Total count of {st_course} is {student_acc_course(st_course)}");
            break;
        elif(choice==5):
            cer_id=int(input("Enter the Id:"));
            certificate_collection(cer_id);
            break;
        elif(choice==6):
            upd_id=int(input("Enter the Id:"));
            update_status(upd_id);
            print("Update the Status");
            break;
        elif(choice==7):
            data_extraction();
            break;
        elif(choice==8):
            sorted_data();
            break;
        elif(choice==9):
            chn_id=int(input("Enter the Id:"));
            chn_cou=input("Enter the course:");
            update_course(chn_id,chn_cou)
            print("Course Updated");
            break;
        elif(choice==10):
            add_id=int(input("Enter id:"));
            add_cou=input("Enter the course:");
            add_course(add_id,add_cou);
            break;
        elif(choice==11):
            col_name=input("Enter column name:");
            string_to_array(col_name);
            break;
        else:
            print("Invalid Choice! Try again.");

if __name__=="__main__":
    main();