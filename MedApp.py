from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the dosages for each medication and indication
dosages = {
    'Acetaminophen': {
        'Fever': 12.5,
        'Pain': 12.5,
    },
    'Amoxicillin': {
        'Otitis media-HD': 90,
        'Otitis media-LD': 45,
        'Sinusitis': 90,
        'Pneumonia': 90,
        'Strep throat': 50
    },
    'Amoxicillin/Clavulanate': {
        'Otitis media-HD': 90,
        'Otitis media-LD': 45,
        'Sinusitis': 90,
        'Pneumonia': 90,
        'Strep throat': 50
    },
    'Azithromycin': {
        'Otitis media': 30,
    },
    'Cefdinir': {
        'Otitis media': 14,
        'Sinusitis': 14,
        'soft tissue infection': 14,
    },
    'Cefpodoxime': {
        'Otitis media': 10,
    },
    'Cephalexin': { 
        'Otitis media': 50,
        'Sinusitis': 50,
        'Pneumonia': 50,
        'Strep throat': 50,
        'Soft tissue infection': 50,
        'UTI': 50
    },
    'Clindamycin': {
        'Otitis media': 30,
        'Sinusitis': 30,
        'Pneumonia': 30,
        'Strep throat': 30,
        'Soft tissue infection': 30 
    },
    'Trimethoprim/Sulfamethoxazole': {
        'Otitis media': 8,
        'Sinusitis': 8,
        'Pneumonia': 8,
        'UTI': 10
    },
    'dexamethasone': {
        'Asthma exacerbation': 0.6,
        'Croup': 0.6
    },
    'prednisolone': {
        'Asthma exacerbation': 2,
        'croup': 2,
    },
    'cyproheptadine': {
        'Appetite stimulant under 7 (max= 12/day)': 0.25,
        'Appetite stimulant 7-14 yrs (max= 16/day)': 0.25,
        'Appetite stimulant over 14 yrs (max= 32/day)': 0.25
    },
    'Fer-in-sol': {
        'Iron deficiency anemia': 4  
    },
}

#Define avilable suspension concentrations
suspensions = {
    'Acetaminophen': ['160mg/5ml'],
    'Amoxicillin': ['125mg/5ml', '200mg/5ml', '250mg/5ml', '400mg/5ml'],
    'Amoxicillin/Clavulanate': ['600mg/5ml'],
    'Azithromycin': ['100mg/5ml', '200mg/5ml'],
    'Cefdinir': ['125mg/5ml', '250mg/5ml'],
    'Cefpodoxime': ['50mg/5ml', '100mg/5ml'],
    'Cephalexin': ['125mg/5ml', '250mg/5ml'],
    'Clindamycin': ['150mg/ml', '75mg/5ml'],
    'Trimethoprim/Sulfamethoxazole': ['40mg/5ml', '80mg/5ml'],
    'dexamethasone': ['0.5mg/5ml'],
    'prednisolone': ['15mg/5ml'],
    'cyproheptadine': ['2mg/5ml'],
    'Fer-in-sol': ['15mg/ml'],
},
#defining the available frequencies
frequencies = {
    'QD': 1,
    'BID': 2,
    'TID': 3,
    'QID': 4,
},

@app.route('/calculate_dosage', methods=['POST'])
def calculate_dosage():
    data = request.get_json()
    medication = data['medication']
    indication = data['indication']
    weight = data['weight']
    suspension = data['suspension']
    Frequency = data['Frequency']

    # Calculate the dosage
    mg_per_day = dosages[medication][indication] * weight
    mg_per_dose = mg_per_day / Frequency 
    ml_per_dose = mg_per_dose / (int(suspension.split('mg')[0]) / 5)

    return jsonify({'ml_per_dose': round(ml_per_dose, 1)})

if __name__ == '__main__':
    app.run(debug=True)
