var inputs = {};

function getInputs() {
  inputs['service'] = $('#service').val();
  inputs['food'] = $('#food').val();
}

$(document).ready(function(){

  $('#calc').click(function(){
    getInputs();
    $.ajax({
        url: '/',
        type: 'POST',
        data: inputs,
        success: function(data) {
            console.log('Wysłano dane wejsciowe');
            $('#input-data').text("Dane wejsciowe")
            $('#service-feed').text("Jakosc obslugi: " + data[0])
            $('#food-feed').text("Jakosc jedzenia: " + data[1])
            $('#tip').text("Wielkosc napiwka: ")},
        error: function(data) {
            console.log('ERROR - dane wejsciowe');
        }
    }); 
  });
});
