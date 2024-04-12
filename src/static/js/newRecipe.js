$(document).ready(function() {
    $('#summernoteDescripcion').summernote();
    $('#summernotePasos').summernote();
});

$('#summernoteDescripcion').summernote({
    height: 150,                 // set editor height
    minHeight: null,             // set minimum height of editor
    maxHeight: null,             // set maximum height of editor
    focus: true                  // set focus to editable area after initializing summernote
});

$('#summernotePasos').summernote({
    height: 300,                 // set editor height
    minHeight: null,             // set minimum height of editor
    maxHeight: null,             // set maximum height of editor
    focus: true                  // set focus to editable area after initializing summernote
});

function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var img = document.querySelector('.img-fluid');
        img.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);
}