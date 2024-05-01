function submitForm() {
    var isChecked = $('#type_user').is(':checked');
    
    $.ajax({
        type: 'POST',
        url: '/',
        data: { checked: isChecked },
        success: function(response) {
            console.log(response);
        }
    });
}