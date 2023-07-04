document.getElementById('calculate-button').addEventListener('click', function() {
    var medication = document.getElementById('medication').value;
    var indication = document.getElementById('indication').value;
    var weight = document.getElementById('weight').value;
    var suspension = document.getElementById('suspension').value;

    fetch('http://localhost:5000/calculate_dosage', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            medication: medication,
            indication: indication,
            weight: weight,
            suspension: suspension
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = 'Dosage: ' + data.ml_per_dose + ' ml/dose';
    });
});
