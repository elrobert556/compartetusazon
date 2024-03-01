window.addEventListener('load', function() {
    // Obtiene todas las imágenes con la clase "resize-image"
    var images = document.querySelectorAll('.img-fluid');

    // Tamaño deseado para las imágenes (en píxeles)
    var desiredWidth = 350;
    var desiredHeight = 200;

    // Itera sobre cada imagen y establece el tamaño deseado
    images.forEach(function(img) {
      img.width = desiredWidth;
      img.height = desiredHeight;
    });
});