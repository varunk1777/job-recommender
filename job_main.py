from flask import Flask, render_template,request,session,flash
import pandas as pd
import numpy as np
from flask_table import Table, Col
import csv
import sqlite3 as sql
import os


#building flask table for showing recommendation results
class Results(Table):
    id = Col('Id', show=False)
    title = Col('Recommendation List')

app = Flask(__name__)
"""
pickfolder0=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=pickfolder0

pickfolder1=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=pickfolder1

pickfolder2=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=pickfolder2

pickfolder3=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=pickfolder3

pickfolder4=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=pickfolder4"""
#Welcome Page
@app.route('/')
def home():
    """pic0=  os.path.join(app.config['UPLOAD_FOLDER'], 'hero.jpg')
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'features-icon-1.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'features-icon-2.png')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], 'features-icon-3.png')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], 'video-placeholder.jpg')
    #return render_template('home.html', user_image1=pic1, user_image2=pic2, user_image3=pic3,user_image4=pic4 )"""
    return render_template('home (1).html')
usrname=""
mail=""
contact_no=""
"""
@app.route('/gohome')
def homepage():
    return render_template('index.html')
"""
pickfolder0=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=pickfolder0
@app.route('/signup')
def new_user():
   pic0 = os.path.join(app.config['UPLOAD_FOLDER'], 'regs.png')
   return render_template('register (1).html',user_image1=pic0)

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['Name']
            global contact_no
            contact_no = request.form['MobileNumber']
            phone = contact_no
            #phonno = request.form['MobileNumber']
            global mail
            mail = request.form['email']
            email = mail
            #email = request.form['email']
            unm = request.form['Username']
            passwd = request.form['password']
            passwd1=request.form['c_password']

            with sql.connect("C:\\Users\\Hp\\Desktop\\Project\\python\\job_db.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users(name,phono,email,username,password)VALUES(?, ?, ?, ?,?)",(nm,phone,email,unm,passwd))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("login.html")
            con.close()

pickfolder1=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=pickfolder1

@app.route('/login')
def user_login():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'log.png')
    return render_template('login.html', user_image2=pic1)


@app.route('/logindetails',methods = ['POST', 'GET'])
def logindetails():

    if request.method == 'POST':
        # session['logged_in'] = True
        global usrname
        usrname = request.form['username']
        passwd = request.form['password']
        print(usrname,passwd)
        # branch1=request.form['branch']
        with sql.connect("C:\\Users\\Hp\\Desktop\\Project\\python\\job_db.db") as con:
            cur = con.cursor()
            cur.execute("SELECT username,password FROM users where username=? ", (usrname,))

            account = cur.fetchall()

            flag=0
            for row in account:
                database_user = row[0]
                database_password = row[1]
                if database_user == usrname and database_password == passwd:
                        cur.execute("SELECT username,branch FROM details WHERE username=?", (usrname,))
                        branch1 = cur.fetchall()
                        for col in branch1:
                            print(col)
                            branch2 = col[1]
                            print(branch2)
                            if branch2 == "Computer Science":
                                flag=1
                                return render_template('ratingCs(1).html')
                            if branch2 == "Electronics`":
                                flag=1
                                return render_template('ratingEle.html')
                            if branch2 == "Mechanical":
                                flag=1
                                return render_template('ratingMech.html')
                        if(flag==0):
                            return render_template('candidate.html',val=usrname)
                else:
                    if(database_user==usrname and database_password!=passwd):
                        palce="Some Error Occured"
                        palce2="Please Enter Valid Credentials!"
                        return render_template('error_page.html')




@app.route('/info-submit',methods = ['POST'])
def addCand():
    if request.method == 'POST':
        try:
            global usrname
            #user=request.form['comment0']
            user = usrname
            fn = request.form['comment1']
            ln = request.form['comment2']
            gen = request.form['comment11']
            dob = request.form['comment3']
            city = request.form['comment4']
            add = request.form['comment5']
            pin = request.form['comment6']
            branch = request.form['comment7']
            ten = request.form['comment8']
            puc = request.form['comment9']
            engi = request.form['comment10']
            with sql.connect("C:\\Users\\Hp\\Desktop\\Project\\python\\job_db.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO details(username,fname,lname,gender,dob,city,address,pincode,branch,tenth,puc,engi)VALUES(?,?, ?, ?, ?,?,?,?, ?, ?, ?,?)",(user,fn,ln,gen,dob,city,add,pin,branch,ten,puc,engi
				))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            if branch=="Computer Science":
                return render_template("ratingCS(1).html")
            elif branch=="Mechanical":
                return render_template("ratingMech.html")
            else:
                return render_template("ratingEle.html")
        con.close()

@app.route('/fb',methods = ['POST', 'GET'])
def fb():
    if request.method == 'POST':
        try:
        # session['logged_in'] = True
            global usrname
            usrname = request.form['username']
            user = usrname
            global mail
            mail = request.form['em']
            email=mail
            global contact_no
            contact_no = request.form['ph']
            phone=contact_no
            message = request.form['msg']
            with sql.connect("C:\\Users\\Hp\\Desktop\\Project\\python\\job_db.db") as con:

                cur = con.cursor()
                cur.execute("INSERT INTO feedback(username,email,contact,message)VALUES(?,?,?,?)",(user,email,phone,message))
                con.commit()
        except:
                con.rollback()
        finally:
                return render_template('candidate.html',val=usrname)


@app.route("/contact")
def contact():
    return render_template('contact_form.html')

@app.route("/contact_us",methods = ['POST','GET'])
def contact_us():
    if request.method=="POST":
        try:
            name1 = request.form['name']
            phone1 = request.form['ph']
            email1 = request.form['em']
            msg1 = request.form['msg']
            with sql.connect("C:\\Users\\Hp\\Desktop\\Project\\python\\job_db.db") as con:

                cur = con.cursor()
                cur.execute("INSERT INTO contact(name,email,phone,message)VALUES(?,?,?,?)",(name1,email1,phone1,msg1))
                con.commit()
        except:
            con.rollback()
        finally:
            return render_template('home (1).html')

@app.route("/feedback")
def feedback():
    return render_template('feedback_form.html',val=usrname,val1=mail,val2=contact_no)

@app.route("/feedback1")
def feedback1():
    return render_template('feedback_form(1).html',val=usrname,val1=mail,val2=contact_no)

@app.route('/fb1',methods=['POST','GET'])
def fb1():
    if request.method == 'POST':
        try:
        # session['logged_in'] = True

            usrname = request.form['username']
            user = usrname

            mail = request.form['em']
            email=mail

            contact_no = request.form['ph']
            phone=contact_no
            message = request.form['msg']
            with sql.connect("C:\\Users\\Hp\\Desktop\\Project\\python\\job_db.db") as con:

                cur = con.cursor()
                cur.execute("INSERT INTO feedback(username,email,contact,message)VALUES(?,?,?,?)",(user,email,phone,message))
                con.commit()
        except:
                con.rollback()
        finally:
                return render_template('home (1).html')


@app.route("/about")
def about():
    return render_template('about_us.html')

@app.route("/user_rating")
def user_rating():
    return render_template('user_rating.html')
#Rating Page
@app.route("/rating", methods=["GET", "POST"])
def rating1():
    if request.method=="POST":
        return render_template('recommendation1.html')
    return render_template('ratingCs(1).html')


#Results Page

@app.route("/recommendation1", methods=["GET", "POST"])
def recommendation1():
    prediction1=""
    prediction1 = ""
    if request.method == 'POST':
        # reading the original dataset
        jobs = pd.read_csv('CS.csv')

        # separating genres for each jobs
        jobs = pd.concat([jobs, jobs.genres.str.get_dummies(sep='|')], axis=1)

        categories = jobs.drop(['title', 'genres', 'jobId', 'DegreeType'], axis=1)

        preferences = []

        Python = request.form.get('Python')
        R = request.form.get('R')
        Hadoop = request.form.get('Hadoop')
        AWS = request.form.get('AWS')
        SQL = request.form.get('SQL')

        preferences.insert(0, int(Python))
        preferences.insert(1, int(R))
        preferences.insert(2, int(Hadoop))
        preferences.insert(3, int(AWS))
        preferences.insert(4, int(SQL))

        

        print('preferences', preferences)

        testdata = {'Python': Python,
                    'R': R,
                    'Hadoop': Hadoop,
                    'AWS': AWS,
                    'SQL': SQL
                    }


        df7 = pd.DataFrame([testdata])

        df7.to_csv('test.csv', mode="w", header=False, index=False)

        import csv
        import math
        import operator

        def euclideanDistance(instance1, instance2, length):
            distance = 0
            for x in range(length):
                distance += (pow((float(instance1[x]) - float(instance2[x])), 2))
            return math.sqrt(distance)

        def getNeighbors(trainingSet, testInstance, k):
            distances = []
            length = len(testInstance) - 1

            for x in range(len(trainingSet)):
                dist = euclideanDistance(testInstance, trainingSet[x], length)
                distances.append((trainingSet[x], dist))
            distances.sort(key=operator.itemgetter(1))
            neighbors = []
            for x in range(k):
                neighbors.append(distances[x][0])
            return neighbors

        def getResponse(neighbors):
            classVotes = {}
            for x in range(len(neighbors)):
                response = neighbors[x][-1]
                if response in classVotes:
                    classVotes[response] += 1
                else:
                    classVotes[response] = 1
            sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
            return sortedVotes[0][0]

        def getAccuracy(testSet, predictions):
            correct = 0
            for x in range(len(testSet)):
                if testSet[x][-1] == predictions[x]:
                    correct += 1
            return (correct / float(len(testSet))) * 100.0

        trainingSet = []
        testSet = []
        with open('CSR.csv', 'r') as csvfile:
            lines = csv.reader(csvfile)
            dataset = list(lines)
            # print(dataset)

            for x in range(len(dataset) - 1):
                for y in range(5):
                    dataset[x][y] = float(dataset[x][y])
                trainingSet.append(dataset[x])

        with open('test.csv', 'r') as csvfile1:
            lines1 = csv.reader(csvfile1)
            # print(lines1)
            dataset1 = list(lines1)
            # print(dataset1)

            for p in range(len(dataset1)):
                for q in range(5):
                    dataset[p][q] = float(dataset[p][q])
                testSet.append(dataset1[p])

        print("trainingset:", trainingSet)
        print("testingset:", testSet)
        # print("1:",len(trainingSet))
        # print("2:",len(testSet))
        k = 1
        predictions = []
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            response = getResponse(neighbors)
            print("\nNeighbors:", neighbors)
            print('\nResponse:', response)

            predictions.append(response)
        # testSet = pd.read_csv('data/test1.csv')
        # accuracy1 = getAccuracy(testSet, predictions)
        # print('Accuracy1: ' + repr(accuracy1) + '%')
        link2=['https://in.linkedin.com/jobs/search?keywords=Data%20Scientist&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
               'https://in.linkedin.com/jobs/search?keywords=Data%20Analyst&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
               'https://in.linkedin.com/jobs/search?keywords=Data%20Architect&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
               'https://in.linkedin.com/jobs/search?keywords=Data%20Administrator&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
               'https://in.linkedin.com/jobs/search?keywords=Cloud%20Engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
               'https://in.linkedin.com/jobs/search?keywords=software%20engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
               'https://in.linkedin.com/jobs/search?keywords=Systems%20Engineering&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
               'https://in.linkedin.com/jobs/search?keywords=Program%20Manager&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
               'https://in.linkedin.com/jobs/search?keywords=technology%20architect&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0']
        if response == "Data Scientist":
            # pred.append(x)
            link1 = "https://www.naukri.com/data-scientist-jobs?k=data%20scientist"
            link3=link2[0]
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[0])
        elif response == "Data Analyst":
            # pred.append(x)
            link1 = "https://www.naukri.com/data-analyst-jobs?k=data%20analyst"
            link3=link2[1]
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[1])
        elif response == "Data Architect":
            # pred.append(x)
            link1 = "https://www.naukri.com/data-architect-jobs?k=data%20architect"
            link3=link2[2]
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[2])
        elif response=="Data Administrator":
            # pred.append(x)
            link1 = "https://www.naukri.com/data-administrator-jobs?k=data%20administrator"
            link3=link2[3]
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[3])
        elif response=="Cloud Engineer":
            link1= "https://www.naukri.com/cloud-engineer-jobs?k=cloud%20engineer"
            link3=link2[4]
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[4])
        elif response=="Software Engineer":
            link1= "https://www.naukri.com/software-engineer-jobs?k=software%20engineer"
            link3=link2[5]
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[5])
        elif response=="Systems Engineering":
            link1="https://www.naukri.com/systems-engineering-jobs?k=systems%20engineering"
            link3=link2[6]
            return render_template('resultpred.html',pred=response, link=link1, link4=link2[6])
        elif response=="Program Manager":
            link1="https://www.naukri.com/program-manager-jobs?k=program%20manager"
            link3=link2[7]
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[7])
        else:
            link1='https://www.naukri.com/technology-architect-jobs?k=technology%20architect'
            link3=link2[8]
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[8])

    
#for electronics
#Results Page
@app.route("/recommendation2", methods=["GET", "POST"])
def recommendation2():
    prediction1=""
    prediction1 = ""
    if request.method == 'POST':

        jobs = pd.read_csv('ELE.csv')

        jobs = pd.concat([jobs, jobs.genres.str.get_dummies(sep='|')], axis=1)

        categories = jobs.drop(['title', 'genres', 'jobId', 'DegreeType'], axis=1)

        preferences = []

        Python = request.form.get('Python')
        MATLAB = request.form.get('MATLAB')
        VLSI = request.form.get('VLSI')
        Digital_Communication = request.form.get('Digital_Communication')
        Analog_Communication = request.form.get('Analog_Communication')

        preferences.insert(0, int(Python))
        preferences.insert(1, int(MATLAB))
        preferences.insert(2, int(VLSI))
        preferences.insert(3, int(Digital_Communication))
        preferences.insert(4, int(Analog_Communication))

        testdata = {'Python': Python,
                    'MATLAB': MATLAB,
                    'VLSI': VLSI,
                    'Digital_Communication': Digital_Communication,
                    'Analog_Communication': Analog_Communication
                    }

        df7 = pd.DataFrame([testdata])

        df7.to_csv('test.csv', mode="w", header=False, index=False)

        import csv
        import math
        import operator

        def euclideanDistance(instance1, instance2, length):
            distance = 0
            for x in range(length):
                distance += (pow((float(instance1[x]) - float(instance2[x])), 2))
            return math.sqrt(distance)

        def getNeighbors(trainingSet, testInstance, k):
            distances = []
            length = len(testInstance) - 1

            for x in range(len(trainingSet)):
                dist = euclideanDistance(testInstance, trainingSet[x], length)
                distances.append((trainingSet[x], dist))
            distances.sort(key=operator.itemgetter(1))
            neighbors = []
            for x in range(k):
                neighbors.append(distances[x][0])
            return neighbors

        def getResponse(neighbors):
            classVotes = {}
            for x in range(len(neighbors)):
                response = neighbors[x][-1]
                if response in classVotes:
                    classVotes[response] += 1
                else:
                    classVotes[response] = 1
            sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
            return sortedVotes[0][0]

        def getAccuracy(testSet, predictions):
            correct = 0
            for x in range(len(testSet)):
                if testSet[x][-1] == predictions[x]:
                    correct += 1
            return (correct / float(len(testSet))) * 100.0

        trainingSet = []
        testSet = []
        with open('ELER.csv', 'r') as csvfile:
            lines = csv.reader(csvfile)
            dataset = list(lines)
            # print(dataset)

            for x in range(len(dataset)):
                for y in range(5):
                    dataset[x][y] = float(dataset[x][y])
                trainingSet.append(dataset[x])

        with open('test.csv', 'r') as csvfile1:
            lines1 = csv.reader(csvfile1)
            # print(lines1)
            dataset1 = list(lines1)
            # print(dataset1)

            for p in range(len(dataset1)):
                for q in range(5):
                    dataset[p][q] = float(dataset[p][q])
                testSet.append(dataset1[p])

        print("trainingset:", trainingSet)
        print("testingset:", testSet)
        # print("1:",len(trainingSet))
        # print("2:",len(testSet))
        k = 1
        predictions = []
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            response = getResponse(neighbors)
            print("\nNeighbors:", neighbors)
            print('\nResponse:', response)

        # testSet = pd.read_csv('data/test1.csv')
        # accuracy1 = getAccuracy(testSet, predictions)
        # print('Accuracy1: ' + repr(accuracy1) + '%')
        link2 = [
            'https://in.linkedin.com/jobs/search?keywords=Electronics%20Engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'https://in.linkedin.com/jobs/search?keywords=Network%20Planning%20Engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'https://in.linkedin.com/jobs/search?keywords=Service%20Engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'https://in.linkedin.com/jobs/search?keywords=electronics%20design%20engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'https://in.linkedin.com/jobs/search?keywords=Desktop%20Support%20Engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'https://in.linkedin.com/jobs/search?keywords=Control%20Systems%20Engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
            'https://in.linkedin.com/jobs/search?keywords=power%20electronics%20engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0']
        if response == "Electronics Engineer":

            link1 = ("https://www.naukri.com/electronics-engineer-jobs?k=electronics%20engineer")
            return render_template('resultpred.html', pred=response, link=link1,link4=link2[0])
        elif response == "Network Planning Engineer":

            link1 = ("https://www.naukri.com/technical-director-jobs?k=technical%20director")
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[1])
        elif response == "Service Engineer":

            link1 = ("https://www.naukri.com/service-engineer-jobs?k=service%20engineer")
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[2])

        elif response=="Electronics Design Engineer ":

            link1 = ("https://www.naukri.com/electronics-design-engineer-jobs?k=electronics%20design%20engineer")
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[3])

        elif response=="Desktop Support Engineer":
            link1 = ("https://www.naukri.com/desktop-support-engineer-jobs?k=desktop%20support%20engineer")
            return render_template('resultpred.html',pred=response,link=link1, link4=link2[4])

        elif response=="Power Electronics Engineer":
            link1 = ("https://www.naukri.com/power-electronics-engineer-jobs?k=power%20electronics%20engineer")
            return render_template('resultpred.html',pred=response,link=link1, link4=link2[6])

        else:
            link1 = ("https://www.naukri.com/control-systems-engineer-jobs?k=control%20systems%20engineer")
            return render_template('resultpred.html', pred="Control Systems Engineer", link=link1, link4=link2[5])



#for mech
#Results Page
@app.route("/recommendation3", methods=["GET", "POST"])
def recommendation3():
    prediction1 = ""
    if request.method == 'POST':

        jobs = pd.read_csv('MECH.csv')

        jobs = pd.concat([jobs, jobs.genres.str.get_dummies(sep='|')], axis=1)

        categories = jobs.drop(['title', 'genres', 'jobId', 'DegreeType'], axis=1)

        preferences = []

        CAD = request.form.get('CAD')
        Solid_Works = request.form.get('Solid_Works')
        Solid_state_mechanic = request.form.get('Solid_state_mechanic')
        Engineering_design = request.form.get('Engineering_design')
        Ansys = request.form.get('Ansys')

        preferences.insert(0, int(CAD))
        preferences.insert(1, int(Solid_Works))
        preferences.insert(2, int(Solid_state_mechanic))
        preferences.insert(3, int(Engineering_design))
        preferences.insert(4, int(Ansys))

        testdata = {'CAD': CAD,
                    'Solid_Works': Solid_Works,
                    'Solid_state_mechanic': Solid_state_mechanic,
                    'Engineering_design': Engineering_design,
                    'Ansys': Ansys
                    }

        df7 = pd.DataFrame([testdata])

        df7.to_csv('test.csv', mode="w", header=False, index=False)

        import csv
        import math
        import operator

        def euclideanDistance(instance1, instance2, length):
            distance = 0
            for x in range(length):
                distance += (pow((float(instance1[x]) - float(instance2[x])), 2))
            return math.sqrt(distance)

        def getNeighbors(trainingSet, testInstance, k):
            distances = []
            length = len(testInstance) - 1

            for x in range(len(trainingSet)):
                dist = euclideanDistance(testInstance, trainingSet[x], length)
                distances.append((trainingSet[x], dist))
            distances.sort(key=operator.itemgetter(1))
            neighbors = []
            for x in range(k):
                neighbors.append(distances[x][0])
            return neighbors

        def getResponse(neighbors):
            classVotes = {}
            for x in range(len(neighbors)):
                response = neighbors[x][-1]
                if response in classVotes:
                    classVotes[response] += 1
                else:
                    classVotes[response] = 1
            sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
            return sortedVotes[0][0]

        def getAccuracy(testSet, predictions):
            correct = 0
            for x in range(len(testSet)):
                if testSet[x][-1] == predictions[x]:
                    correct += 1
            return (correct / float(len(testSet))) * 100.0

        trainingSet = []
        testSet = []
        with open('MECHR.csv', 'r') as csvfile:
            lines = csv.reader(csvfile)
            dataset = list(lines)
            # print(dataset)

            for x in range(len(dataset) - 1):
                for y in range(5):
                    dataset[x][y] = float(dataset[x][y])
                trainingSet.append(dataset[x])

        with open('test.csv', 'r') as csvfile1:
            lines1 = csv.reader(csvfile1)
            # print(lines1)
            dataset1 = list(lines1)
            # print(dataset1)

            for p in range(len(dataset1)):
                for q in range(5):
                    dataset[p][q] = float(dataset[p][q])
                testSet.append(dataset1[p])

        print("trainingset:", trainingSet)
        print("testingset:", testSet)
        # print("1:",len(trainingSet))
        # print("2:",len(testSet))
        k = 1
        predictions = []
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            response = getResponse(neighbors)
            print("\nNeighbors:", neighbors)
            print('\nResponse:', response)

            predictions.append(response)
        link2 = [
            'https://in.linkedin.com/jobs/search?keywords=Mechanical%20Engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'https://in.linkedin.com/jobs/search?keywords=Powertrain%20Enginer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'https://in.linkedin.com/jobs/search?keywords=Instrumentation%20Engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'https://in.linkedin.com/jobs/search?keywords=automation%20Engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'https://in.linkedin.com/jobs/search?keywords=Mechanical%20Design%20engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'https://in.linkedin.com/jobs/search?keywords=Product%20Engineer&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0']
        # testSet = pd.read_csv('data/test1.csv')
        # accuracy1 = getAccuracy(testSet, predictions)
        # print('Accuracy1: ' + repr(accuracy1) + '%')
        if response == "Mechanical Enginer":
            link1 = "https://www.naukri.com/mechanical-enginer-jobs?k=mechanical%20enginer"
            return render_template('resultpred.html', pred=response, link=link1,link4=link2[0])
        elif response == "Powertrain Enginer":

            link1 = "https://www.naukri.com/mechanical-enginer-jobs?k=powertrain%20enginer"
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[1])
        elif response == "Instrumentation Engineer":

            link1 = "https://www.naukri.com/mechanical-enginer-jobs?k=Instrumentation%20enginer"
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[2])

        elif response=="Automation Engineer":

            link1 = ("https://www.naukri.com/mechanical-enginer-jobs?k=automation%20enginer")
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[3])

        elif response=="Mechanical Design Engineer":
            link1 = ("https://www.naukri.com/mechanical-design-engineer-jobs?k=mechanical%20design%20engineer")
            return render_template('resultpred.html', pred=response, link=link1, link4=link2[4])

        else:
            link1= ("https://www.naukri.com/product-engineer-jobs?k=product%20engineer")
            return render_template('resultpred.html', pred="Product Engineer", link=link1, link4=link2[5])


        
@app.route('/predictinfo')
def predictin():
   return render_template('info.html')



if __name__ == '__main__':
   app.run(debug = True)
