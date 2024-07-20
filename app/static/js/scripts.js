document.addEventListener('DOMContentLoaded', () => {
    const cityInput = document.getElementById('city');
    const suggestionsContainer = document.getElementById('suggestions-container');

    cityInput.addEventListener('input', async () => {
        const query = cityInput.value.trim();

        if (query.length < 2) {
            suggestionsContainer.innerHTML = '';
            return;
        }

        try {
            const response = await fetch(`/autocomplete?query=${encodeURIComponent(query)}`);
            if (response.ok) {
                const suggestions = await response.json();
                suggestionsContainer.innerHTML = suggestions.map(city => 
                    `<div class="suggestion-item list-group-item list-group-item-action">${city}</div>`
                ).join('');

                document.querySelectorAll('.suggestion-item').forEach(item => {
                    item.addEventListener('click', () => {
                        cityInput.value = item.textContent;
                        suggestionsContainer.innerHTML = '';
                    });
                });
            } else {
                console.error('Ошибка получения подсказок:', response.statusText);
            }
        } catch (error) {
            console.error('Ошибка получения подсказок:', error);
        }
    });
});
