$(document).ready(function(){
    $('#hr_up').click(function(){
        $('#h_rate').val(parseInt($('#h_rate').val()) + 1);
    });
    
    $('#hr_down').click(function(){
        $('#h_rate').val(parseInt($('#h_rate').val()) - 1);
    });
    
    $('#speed_up').click(function(){
        new_val=parseFloat($('#speed').val()) + 0.5
        $('#speed').val(new_val.toFixed(1));
    });
    
    $('#speed_down').click(function(){
        new_val=parseFloat($('#speed').val()) - 0.5
        $('#speed').val(new_val.toFixed(1));
    });
    
});
