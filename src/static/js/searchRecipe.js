document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchInput').addEventListener('input', function() {
        var searchText = this.value.trim();
        var cards = document.querySelectorAll('.card');
        
        cards.forEach(function(card) {
            var recipeTitle = card.querySelector('.card-title').innerText.toLowerCase();
            if (recipeTitle.includes(searchText.toLowerCase())) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});

function cambiarIcono() {
    var icono = document.getElementById("icono");
    var iconoInput = document.getElementById("iconoInput");
    
    if (icono.classList.contains("fa-regular")) {
      icono.classList.remove("fa-regular");
      icono.classList.add("fa-solid");
      iconoInput.value = "fa-solid"; // Actualizar el valor del input hidden
    } else {
      icono.classList.remove("fa-solid");
      icono.classList.add("fa-regular");
      iconoInput.value = "fa-regular"; // Actualizar el valor del input hidden
    }
  }