from flask import Flask , request  ,render_template , url_for ,redirect , flash
import random
app=Flask(__name__)


app.secret_key="thisismyabcdsecretkey123321"

@app.route('/',methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/pass_gen",methods=["POST","GET"])
def gen_pass():
    j=1
    number,character=[],[]
    password=''
    no,ch=1,1
    try:
        no=int(request.form.get('digit'))
        ch=int(request.form.get('char'))
    except ValueError:
        flash("please enter something")
    charac=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','@','#','$','&']
    num=['0','1','2','3','4','5','6','7','8','9']
    full=charac+num
    length=no+ch
    if length<8:
        flash("Length must be of atleast 8 characters")
        return redirect(url_for('home'))
    
    for i in range(no):
        number.append(random.choice(num))
    for i in range(ch):
        character.append(random.choice(charac))
    
    password=number+character
    
    random.shuffle(password)
    password="".join([str(elm) for elm in password])
    return render_template('index.html',password=password)

if __name__=="__main__":
    app.run(debug=True)
        
    
    

