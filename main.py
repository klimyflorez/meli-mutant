from flask import Flask, request, jsonify
from sqlalchemy import true
from helper.isMutant import IsMutant
from flask_sqlalchemy import SQLAlchemy
from models.Stats import Stast

app = Flask(__name__)

app.config['SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Mutants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/mutant/', methods=['POST'])
def isMutant():
    try:
        data = request.get_json()
        id = ''.join(data['dna'])
        #data = Stats.query.filter_by(_id=id).first()
        result = IsMutant(data['dna'])
        if result.isMutant:
            stat = Stast(id,result.isMutant)
            db.session.add(stat)
            db.session.commit()
            return {
                'id':id,
                'isMutant': result.isMutant,
                'result': '{0:2.2f}%'.format((result.count_mutant_dna * 100) / result.size),
                'message': "Magneto quiere saber tu ubicación",
            }, 200
        else:            
            stat = Stast(id,result.isMutant)
            db.session.add(stat)
            db.session.commit()

            if result.error.get('error'):
                return result.error, 406 
            else:
                return {}, 403
    except Exception as err:
        print(err)
        return {'Error in mutation request': 'err'}

@app.route('/stats/', methods=['GET'])
def getStats():    
    isMutant = db.session.query(Stast).filter(Stast.is_mutant == True).count()
    if isMutant > 0:
        isHuman = db.session.query(Stast).filter(Stast.is_mutant == False).count()
        ratio = '{0:2.2f}%'.format( (isMutant * 100) / (isMutant+isHuman))        
        return {
                'count_mutant_dna': isMutant,
                'count_human_dna': isHuman,
                'ratio': ratio,
            }
    else:
        return {
            'Error': True,
            'Message': 'First enter the DNA sequence'
            }


if __name__ == '__main__':
    db.create_all()    
    app.run(debug=True)