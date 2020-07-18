from flask import Flask , render_template , request , url_for, flash
import random

app=Flask(__name__)
app.secret_key="riharshamsimkauran"
user_score,comp_score=0,0
turn=1
user=''

def win(user_score,comp_score):
    if turn==5:
        if user_score > comp_score:
            return True
        else:
            return False
def lost(user_score,comp_score):
    if turn==5:
        if user_score < comp_score:
            return True
        else:
            return False

@app.route('/')
@app.route('/play',methods=['GET','POST'])
def play():
    i=0
    global user_score
    global comp_score
    global turn
    global user

    var=["stone","paper","scissor"]
    comp=random.choice(var)              # returns a random item from the list
    
    if win(user_score,comp_score):
        flash('Hurray You won','success')
        
    elif lost(user_score,comp_score):
        flash('Oops You lost','danger')

    elif turn==5 and (user_score==comp_score):
        turn-=1

    if turn <=5:

        if request.form.get('stone'):
            user='stone'
            if (user=='stone' and comp=='paper'):
                comp_score+=1
                turn+=1
            elif user=='stone' and comp=='scissor':
                user_score+=1
                turn+=1
            else:
                turn=turn
                user_score=user_score
                comp_score=comp_score
                   
           
            return render_template('play.html',user=user,user_score=user_score , comp_score=comp_score , comp=comp,turn=turn)

        elif request.form.get('paper'):
            user='paper'
            if (user=='paper' and comp=='scissor'):
                comp_score+=1
                turn+=1
            elif user=='paper' and comp=='stone':
                user_score+=1
                turn+=1
            else:
                turn=turn
                user_score=user_score
                comp_score=comp_score
                    
             
            return render_template('play.html',user=user,user_score=user_score , comp_score=comp_score , comp=comp,turn=turn)

        elif request.form.get('scissor'):
            user='scissor'
            if (user=='scissor' and comp=='stone'):
                comp_score+=1
                turn+=1
            elif user=='scissor' and comp=='paper':
                user_score+=1
                turn+=1
            else:
                turn =turn
                user_score=user_score
                comp_score=comp_score
                      
            return render_template('play.html',user=user,user_score=user_score , comp_score=comp_score , comp=comp,turn=turn)
    else:
        if request.form.get('paper') or request.form.get('stone') or request.form.get('scissor'):
            flash("Game over, click on 'Play Again' button to restart the match",'dark')
            return render_template('play.html',user=user,user_score=user_score , comp_score=comp_score , comp=comp,turn=turn)
            
    if request.method == 'GET':
        return render_template('play.html',user=user,user_score=user_score , comp_score=comp_score , comp=comp,turn=turn)
       
@app.route('/again')
def again():
    global user_score
    global comp_score
    global turn
    user_score,comp_score=0,0
    turn =1
    return render_template("play.html",user_score=user_score, comp_score=comp_score, turn=turn)

if __name__=="__main__":
    app.run(debug=True)