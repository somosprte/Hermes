    $(document).ready(function(){
    	$('.parallax').parallax();
    	$('select').material_select();
    	$('.modal').modal();
    });


    $('.chk').change(function(){
    	if($(this).is(":checked")){
    		enviar($("#select").val(), this.id,"ON");
    	}else{
    		enviar($("#select").val(), this.id,"OFF");
    	}
    })

    $('#select').change(function(){
    	if(this.value == 'BASE'){
    		$('.chk').attr('disabled', true);
    		$('#COM').attr('disabled', false);
    	}
    	else{
    		$('.chk').attr('disabled', false);
    	}
    })


    function enviar(device,led,status) {
    	$.ajax({
    		url: `http://177.15.78.152:5000/hermes/${device}`,
    		method: 'POST',
    		data: `data=DO ${led} ${status}`,
    	})
    	.done(function() {
    		console.log("success");
    	})
    	.fail(function() {
    		console.log("error");
    	})
    	.always(function() {
    		console.log("complete");
    	});
    }
