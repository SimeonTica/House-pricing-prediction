function predictPrice() {

    var area = parseFloat(document.getElementById('area').value);
    var bedrooms = parseInt(document.getElementById('bedrooms').value);
    var bathrooms = parseInt(document.getElementById('bathrooms').value);

    var predictedPrice = 

    document.getElementById('result').innerText = 'Predicted Price: ' + predictedPrice.toFixed(2);
}
