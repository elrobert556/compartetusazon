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